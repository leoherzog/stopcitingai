# Contributing

Thanks for your interest in improving Stop Citing AI! This project is a static site, so most contributions are new or improved translations. Here's how to propose yours:

## 1. Pick a Locale

- Prefer [BCP 47 language tags](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) with hyphens (e.g. `fr-FR`, `pt-BR`, `de-DE`) for directory names and HTML `lang` attributes. A language-only tag (e.g. `es/`, `fr/`) also works if the translation is intended for all dialects of that language.
- If a more specific locale already exists (for example `es-AR/`), choose whether your translation should live alongside it (e.g. a new `es/`) or replace/refresh it. Avoid duplicate copies of the same locale.
- When updating an existing translation, edit its current `index.html` instead of creating a new directory.

## 2. Copy the Base Page

1. Create a folder at the repository root named after your locale, such as `fr/`.  
2. Copy [the English root `index.html`](https://github.com/leoherzog/stopcitingai/blob/main/index.html) into the new folder.

## 3. Translate the Content

- Translate only human-facing text (headings, paragraphs, button labels, aria labels, etc.).
- Keep HTML structure, element attributes, and Pico CSS classes exactly the same.
- Update metadata that includes text in the `<head>`, including:
  - `<html lang="…">`
  - `<title>` and `<meta name="description">`
  - Open Graph (`og:title`, `og:description`, `og:locale`) and Twitter card fields
- **Important locale format difference:**
  - Use **hyphens** in: directory names (`fr/` or `fr-FR/`), `<html lang="fr-FR">`, and Twitter card locale
  - Use **underscores** in: `og:locale` meta tags (`og:locale="fr_FR"`)
  - Examples: For Argentina Spanish, use directory `es-AR/`, set `<html lang="es-AR">`, but set `<meta property="og:locale" content="es_AR" />`
- For language-only directories, set `<html lang>` to the two-letter code with a hyphen format (e.g. `fr`) and `og:locale` with underscores (e.g. `fr_FR`) so the generic translation is recognized correctly.
- Leave URLs, query parameters, and file paths unchanged unless you have a specific reason to update them for your locale.
- If you use localized punctuation (e.g. «guillemets») or decimal separators, be consistent throughout the page.
- Add your locale to the language selector in all other locale pages (for example, add `<option value="fr">Français</option>`) to all other `index.html` files.
- Add your URL to the sitemap (`sitemap.xml`) before the closing `</urlset>` tag, for example:
  ```xml
  <url>
    <loc>https://stopcitingai.com/fr/</loc>
  </url>
  ```

## 4. Proofread and Preview

- Read the page end-to-end to ensure grammar, spelling, and tone feel natural for the locale.  
- Preview locally by serving the repository root (for example, run `python -m http.server 8000` in the project folder and visit `http://localhost:8000/<locale>/`).

## 5. Submit a Pull Request

Include the following in your PR description:

- Locale code (e.g. `fr`) and language name in English plus the locale language (`Français`).
- Any open questions or items you are unsure about.

When you open the PR:

- Verify the locale directory and file names match your locale tag.  
- Ensure there are no unrelated changes.  
- Mention any collaborators who helped review the translation.

## Need Help?

Feel free to open a GitHub Issue titled “Translation: <locale>” to coordinate with others before you start. If a phrase doesn't have an obvious translation, leave the English and add a comment/question in your PR so we can workshop it together!