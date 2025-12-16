#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "jinja2",
# ]
# ///
"""
Build script for stopcitingai.com

Generates static HTML files from Jinja templates and JSON translation files.
Inlines all assets (CSS, JS, fonts) for self-contained HTML pages.

Run with: uv run build.py
"""

import base64
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


# Font configuration per language
FONT_CONFIG = {
    'caveat': {
        'file': 'fonts/caveat-v23-cyrillic_cyrillic-ext_latin_latin-ext-700.woff2',
        'family': 'Caveat',
        'weight': 700,
    },
    'klee-one': {
        'file': 'fonts/klee-one-v13-japanese-600.woff2',
        'family': 'Klee One',
        'weight': 600,
    },
}

def load_font_base64(font_path: Path) -> str:
    """Load a font file and return its base64-encoded content."""
    return base64.b64encode(font_path.read_bytes()).decode('ascii')


SITE_URL = 'https://stopcitingai.com'

# HTML template for the AI model name (used in rotating display)
# Note: quotes escaped for JSON string replacement
AI_SPAN = '<span class=\\"ai\\">ChatGPT</span>'


def build():
    """Build all HTML files from templates and translations."""
    root = Path(__file__).parent
    public_dir = root / 'public'

    # Clean and recreate public directory
    if public_dir.exists():
        shutil.rmtree(public_dir)
    public_dir.mkdir()

    # Set up Jinja environment
    env = Environment(
        loader=FileSystemLoader(root / 'templates'),
        autoescape=False,  # We handle escaping manually for HTML content
    )
    template = env.get_template('index.html.jinja')

    # Load fonts as base64
    fonts = {}
    for font_key, config in FONT_CONFIG.items():
        fonts[font_key] = load_font_base64(root / config['file'])

    # Load assets to inline
    pico_css = (root / 'pico.min.css').read_text(encoding='utf-8')
    lang_js = (root / 'lang.js').read_text(encoding='utf-8')

    # Load all translations and build languages list
    translations_dir = root / 'translations'
    translations = []
    languages = []
    for json_file in sorted(translations_dir.glob('*.json')):
        raw = json_file.read_text(encoding='utf-8').replace('{ai}', AI_SPAN)
        data = json.loads(raw)
        translations.append(data)
        languages.append({
            'code': data['lang'],
            'name': data['language_name'],
        })

    # Build each language
    built_languages = []
    for data in translations:
        lang = data['lang']
        font_key = data.get('font', 'caveat')
        font_config = FONT_CONFIG[font_key]

        print(f'Building {lang}...')

        html = template.render(
            **data,
            font_data=fonts[font_key],
            font_family=font_config['family'],
            font_weight=font_config['weight'],
            pico_css=pico_css,
            lang_js=lang_js,
            languages=languages,
        )

        # Output path: English at root, others in subdirectories
        if lang == 'en':
            out_path = public_dir / 'index.html'
        else:
            out_dir = public_dir / lang
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / 'index.html'

        out_path.write_text(html, encoding='utf-8')
        print(f'  -> {out_path.relative_to(root)}')
        built_languages.append(lang)

    # Generate sitemap
    sitemap_template = env.get_template('sitemap.xml.jinja')
    sitemap = sitemap_template.render(site_url=SITE_URL, languages=sorted(built_languages))
    (public_dir / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    print('Generated sitemap.xml')

    # Copy static assets
    static_assets = ['favicon.svg', 'social.png', 'robots.txt']
    for asset in static_assets:
        src = root / asset
        if src.exists():
            shutil.copy(src, public_dir / asset)
            print(f'Copied {asset}')

    print(f'\nBuild complete! Output in {public_dir.relative_to(root)}/')


if __name__ == '__main__':
    build()
