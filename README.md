# 🌐 FHIR IG Translation Utilities

Tools for managing and checking status of translations in the **FHIR Implementation Guide (IG) ecosystem**.

---

# 🌐 FHIR IG Translation Utilities

This repository provides tools for managing and visualizing translations in the **FHIR Implementation Guide (IG) ecosystem**.

It supports `.po`-based localization workflows such as those used by `sushi`, IG Publisher, and related tooling.

---

## 📊 Translation Status Dashboard – [`translation-status/`](./translation-status/)

An automated dashboard that visualizes `.po` translation coverage across languages and files.
Has an interactive stacked bar chart showing the translations that are done and reviewed, for review, or not done.
Downloadable [`stats.csv`](https://fhir.github.io/translation-utils/stats.csv) and [`stats.json`](https://fhir.github.io/translation-utils/stats.json)

See [Dashboard](https://fhir.github.io/translation-utils/)  

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

## 📄 License

[MIT](./LICENSE)

---

## 🤝 Contributions

Contributions welcome! Add utilities, improve analysis, or suggest better workflows for multilingual IG maintenance.

---
