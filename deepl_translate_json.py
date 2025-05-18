import json
import re
import time
import sys
import os
import requests

# === DeepL API Key (set via env variable or directly below) ===
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY") or "2fa4...2:fx"



if DEEPL_API_KEY == "YOUR_DEEPL_API_KEY":
    print("❗ Set your DeepL API key via environment variable 'DEEPL_API_KEY' or hardcode it.")
    sys.exit(1)

def deepl_translate(text, target_lang):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "source_lang": "EN",
        "target_lang": target_lang.upper()
    }
    response = requests.post(url, data=params)
    response.raise_for_status()
    return response.json()["translations"][0]["text"]

def protect_placeholders(text):
    placeholders = re.findall(r"%[^% ]+%", text)
    protected = text
    for i, ph in enumerate(placeholders):
        protected = protected.replace(ph, f"[PH{i}]")
    return protected, placeholders

def restore_placeholders(text, placeholders):
    restored = text
    for i, ph in enumerate(placeholders):
        restored = restored.replace(f"[PH{i}]", ph)
    return restored

# 🟡 Command-line arguments
if len(sys.argv) < 3:
    print("Usage: python translate_json_deepl.py <input-file.json> <target-lang>")
    sys.exit(1)

input_path = sys.argv[1]
target_lang = sys.argv[2]  # e.g. pt, fr, nl

filename = os.path.basename(input_path)
basename = os.path.splitext(filename)[0]
output_folder = os.path.join("translated", target_lang)
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, f"{basename}-{target_lang}.json")

# 🔄 Load and translate
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

en_strings = data.get("en", {})
lang_strings = data.get(target_lang, {})

for key, en_value in en_strings.items():
    if key not in lang_strings or not lang_strings[key].strip():
        print(f"🔄 Translating [{key}]: {en_value}")
        try:
            protected, placeholders = protect_placeholders(en_value)
            translated = deepl_translate(protected, target_lang)
            final = restore_placeholders(translated, placeholders)
            lang_strings[key] = final
            print(f"   ✅ → {final}")
            time.sleep(0.2)
        except Exception as e:
            print(f"   ⚠️  Failed to translate '{key}': {e}")
    else:
        print(f"⏭️  Skipped [{key}], already translated.")

# 💾 Save result
data[target_lang] = lang_strings
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Saved to {output_path}")
