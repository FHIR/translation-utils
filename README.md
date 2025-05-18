# Translation utils

A Python script to translate `.po` files using DeepL or Google Translate, based on a configuration file. It supports translating a single file or all `.po` files in a specified directory.

## 📋 Features

Translates `.po` files from English to a specified target language.

Utilizes DeepL API if a key is provided; otherwise, defaults to Google Translate.

Processes a single file or all `.po` files in a given directory.

Prevents line wrapping in output `.po` files to maintain formatting.

## 🐍 Prerequisites

Python 3.11.x  -- NOT 3.13!!!

`pip` (Python package installer)

## 🧰 Installation

### 1. Install Python 3.11

#### Windows

Download the Python 3.11 installer from the official website.

Run the installer and ensure you check the box "Add Python to PATH" during installation.

Verify the installation:

```bash
python --version
```

#### macOS

Install Homebrew if you haven't already:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Use Homebrew to install Python 3.11:

```bash
brew install python@3.11
```

Verify the installation:

```bash
python3.11 --version
```

#### Linux (Ubuntu)

Add the Deadsnakes PPA:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```

Install Python 3.11:

```bash
sudo apt install python3.11 python3.11-venv python3.11-dev
```

Verify the installation:

```bash
python3.11 --version
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.   
**This is essential if you have more recent versions of Python installed as well.**

Create a virtual environment:

```bash
python3.11 -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Upgrade `pip`:

```bash
pip install --upgrade pip
```

Install required packages:

```bash
pip install polib deepl deep-translator
```

## ⚙️ Configuration

Create a `config.json` file in the same directory as `translate_po.py`. This file should contain the following keys:

```json
{
"deepl_api_key": "your-deepl-api-key", // Optional: If omitted, Google Translate will be used
"deepl_lang": "pt-PT", // Optional: Specific DeepL target language code
"output_lang": "pt", // Required: Output language code (e.g., 'pt')
"input_folder": "c:\\your\\folder" // Optional: Folder containing .po files
}
```

`deepl_api_key`: Your DeepL API key. If not provided, the script will use Google Translate.

`deepl_lang`: The specific language code for DeepL translations (e.g., 'pt-PT'). If not provided, `output_lang` will be used.

`output_lang`: The language code for the output translations. This determines the subdirectory under `translated/` where the translated files will be saved.

`input_folder`: The directory containing `.po` files to translate. If not specified, you must provide a file path using the `--file` argument.

## 🚀 Usage

Activate your virtual environment before running the script:

```bash

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate
```

### Translate All `.po` Files in a Folder

```bash
python translate_po.py --config config.json
```

### Translate a Single `.po` File

```bash
python translate_po.py --config config.json --file path/to/file.po
```

## 📝 Notes

Translated files will be saved in the `translated/<output_lang>/` directory.

The script skips entries that already have translations (`msgstr` is not empty).

A delay (`time.sleep(0.3)`) is included between translations to respect API rate limits.

## 📄 License

This project is licensed under the MIT License.