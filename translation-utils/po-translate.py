import os
import sys
import json
import time
import polib
import argparse
from pathlib import Path
from datetime import datetime

try:
    import deepl
except ImportError:
    deepl = None

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_translator(config):
    if 'deepl_api_key' in config and config['deepl_api_key']:
        if deepl is None:
            raise ImportError("deepl module not installed. Install it with 'pip install deepl'")
        return 'deepl', deepl.Translator(config['deepl_api_key'])
    else:
        if GoogleTranslator is None:
            raise ImportError("deep_translator module not installed. Install it with 'pip install deep-translator'")
        return 'google', None

def translate_text(text, translator_type, translator, target_lang):
    if translator_type == 'deepl':
        result = translator.translate_text(text, target_lang=target_lang)
        return result.text
    else:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)

def process_po_file(po_path, output_path, translator_type, translator, target_lang):
    po = polib.pofile(po_path, wrapwidth=0)
    total = len(po)
    count = 0

    # Set metadata
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M+0000')
    po.metadata = {
        'Project-Id-Version': 'FHIR',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': now,
        'PO-Revision-Date': now,
        'Language': target_lang,
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Transfer-Encoding': '8bit'
    }

    for entry in po:
        count += 1
        if not entry.msgstr.strip():
            print(f"[{count}/{total}] Translating: {entry.msgid}")
            try:
                translated = translate_text(entry.msgid, translator_type, translator, target_lang)
                entry.msgstr = translated
                print(f"      → {translated}")
                time.sleep(0.3)  # To respect API rate limits
            except Exception as e:
                print(f"      ⚠️  Failed: {e}")
        else:
            print(f"[{count}/{total}] Skipped (already translated): {entry.msgid}")

    po.save(output_path)
    print(f"\n✅ Done. Translated entries saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Translate .po files using DeepL or Google Translate.")
    parser.add_argument('-c', '--config', required=False, help="Path to the configuration JSON file.")
    parser.add_argument('-f', '--file', help="Path to a single .po file to translate.")
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_config("config.json")

    translator_type, translator = get_translator(config)

    input_folder = config.get('input_folder')
    output_lang = config.get('output_lang')
    target_lang = config.get('deepl_lang', output_lang)

    if not output_lang:
        print("❌ 'output_lang' must be specified in the configuration.")
        sys.exit(1)

    output_folder = Path('translated') / output_lang
    output_folder.mkdir(parents=True, exist_ok=True)

    po_files = []

    if input_folder:
        input_path = Path(input_folder)
        if not input_path.is_dir():
            print(f"❌ Input folder '{input_folder}' does not exist.")
            sys.exit(1)
        po_files = list(input_path.rglob('*.po'))
    elif args.file:
        po_files = [Path(args.file)]
    else:
        print("❌ Either 'input_folder' in config or '--file' argument must be specified.")
        sys.exit(1)

    for po_file in po_files:
        relative_path = po_file.relative_to(po_file.parents[1]) if input_folder else po_file.name
        output_path = output_folder / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        process_po_file(po_file, output_path, translator_type, translator, target_lang)

if __name__ == "__main__":
    main()
