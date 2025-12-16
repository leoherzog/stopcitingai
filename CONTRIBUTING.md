# Contributing

Thanks for your interest in improving Stop Citing AI! This project uses a build system that generates HTML from JSON translation files. Most contributions are new or improved translations. Here's how to propose yours:

## 1. Pick a Locale

- Use [BCP 47 language tags](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) (e.g. `fr`, `pt-BR`, `de-DE`) for the filename and `lang` field.
- If a more specific locale already exists (for example `es-AR.json`), choose whether your translation should live alongside it (e.g. a new `es.json`) or replace/refresh it.
- When updating an existing translation, edit its JSON file directly.

## 2. Create or Copy a Translation File

1. Look in the `translations/` folder for existing translations.
2. Copy `translations/en.json` to a new file named after your locale, such as `translations/fr.json`.

## 3. Translate the Content

Edit your new JSON file:

- **`lang`**: Set to your BCP 47 language tag (e.g. `"fr"` or `"fr-CA"`)
- **`locale`**: Set to the locale with underscores for Open Graph (e.g. `"fr_FR"` or `"fr_CA"`)
- **`language_name`**: The display name for the language selector (e.g. `"Français"` or `"Français (Canada)"`)
- **`font`**: Usually `"caveat"` (Latin/Cyrillic scripts) or `"klee-one"` (Japanese)
- **`ai_models`**: Optionally add region-specific AI models to the rotating list
- **`strings`**: Translate all user-facing text
- **`further_reading`**: Optionally translate article titles or add locale-specific sources

### Translation Tips

- Translate only the string values, not the JSON keys.
- Use `{ai}` as a placeholder for the AI model name (it rotates between ChatGPT, Claude, etc.). Example: `"But {ai} Said…"`
- Use proper typographic quotes for your language in `but_ai_said` and `share_cta_quote`:
  - English/Spanish/Dutch/Chinese: `&ldquo;` and `&rdquo;` (curly quotes)
  - French/Russian: `«guillemets»`
  - German: `„low-high"` quotes
  - Japanese: `「corner brackets」`
- Keep HTML tags like `<mark>`, `<em>`, `<strong>` in place.
- The `og_image_alt` and `twitter_image_alt` should describe the social sharing image in your language.

## 4. Build and Preview

Run the build script to generate HTML from your translation:

```bash
uv run build.py
```

Then preview locally:

```bash
cd public && python -m http.server 8000
```

Visit `http://localhost:8000/` (English) or `http://localhost:8000/<locale>/` for other languages.

## 5. Submit a Pull Request

Include in your PR description:

- Locale code (e.g. `fr`) and language name in English plus the native name (e.g. `French / Français`)
- Any open questions or phrases you're unsure about

When you open the PR:

- Verify your JSON file is valid (the build script will fail if not)
- Ensure there are no unrelated changes
- Mention any collaborators who helped review the translation

## Need Help?

Feel free to open a GitHub Issue titled "Translation: \<locale\>" to coordinate with others before you start. If a phrase doesn't have an obvious translation, leave the English and add a comment/question in your PR so we can workshop it together!
