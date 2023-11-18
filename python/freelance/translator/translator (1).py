import re
from googletrans import Translator
from file import input_text
def find_word(input_text):

    pattern = r'msgid "(.*?)"'
    match = re.search(pattern, input_text)
    if match:
        msgid_value = match.group(1)
        return msgid_value
    else:
        return "msgid not found"




def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def add_word(input_text, word):

    pattern = r'msgid "(.*?)"\nmsgstr "(.*?)"'
    match = re.search(pattern, input_text)
    if match:
        msgid_value = match.group(1)
        msgstr_value = match.group(2)
        new_msgstr_value = f'"{msgstr_value} {word}"'
        updated_text = re.sub(pattern, fr'msgid "{msgid_value}"\nmsgstr {new_msgstr_value}', input_text)
        return updated_text
    else:
        print("msgid and msgstr not found")


def group_separator(input_text):
    pattern = r'\n\n'
    items = re.split(pattern, input_text.strip())

    translations = []
    for item in items:
        match = re.search(r'#:.*?\nmsgid "(.*?)"\nmsgstr "(.*?)"', item)
        if match:
            translation = f"{match.group(0)}"
            translations.append(translation)
    return translations




texts = group_separator(input_text=input_text)
for i in texts:
    word = find_word(i)
    word_translate = translate_text(word)
    full_word = add_word(i, word_translate)

    my_file = open("скинь_это_мне_брат.txt", "a", encoding="utf-8")
    my_file.write(f"\n\n{full_word}")
    my_file.close()