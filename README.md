# 🌐 FHIR IG Translation Utilities

This repository provides tools for managing and visualizing translations in the **FHIR Implementation Guide (IG) ecosystem**.

It supports `.po`-based localization workflows such as those used by `sushi`, IG Publisher, and related tooling.

---

## 📊 Translation Status Dashboard – [`translation-status/`](./translation-status/)

An automated dashboard that visualizes `.po` translation coverage across languages and files.

### 🔍 Features:
- Interactive stacked bar chart (translated, fuzzy, untranslated)
- Hoverable tooltips with percentages and raw counts
- Table of all translation stats per file and language
- Downloadable CSV and JSON stats
- GitHub Pages–ready (`gh-pages` branch)

📁 See [`translation-status/`](./translation-status/) for usage and structure.  
🌍 View the live dashboard:  
`https://fhir.github.io/translation-utils/`

---

## 🤖 Translation Assistant – [`po-translate/`](./po-translate/)

A command-line tool to automatically translate `.po` files using DeepL or Google Translate.

### 🔍 Features:
- Fills in missing translations
- Marks machine-translated entries as `# fuzzy`
- Respects existing translations
- Optional profile for batch translation of IG `.po` folders

📁 See [`po-translate/`](./po-translate/) for usage instructions and API key setup.

---

## 🧱 Project Structure

```
translation-utils/
├── translation-status/ # Dashboard generator (Python, HTML)
│ └── README.md
├── po-translate/ # CLI translation tool using AI services
│ └── README.md
└── README.md # This file
```

---

## 🛠 Use Cases

- National/regional IG publishers managing localization
- Translators reviewing `.po` progress across multiple files
- CI workflows generating dashboards for multilingual IGs

---

## 📄 License

[MIT](./LICENSE)

---

## 🤝 Contributions

Contributions welcome! Add utilities, improve analysis, or suggest better workflows for multilingual IG maintenance.
