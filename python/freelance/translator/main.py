import re
from googletrans import Translator

def find_word(input_text):

    pattern = r'msgid "(.*?)"'
    match = re.search(pattern, input_text)
    if match:
        msgid_value = match.group(1)
        # print(msgid_value)
        return msgid_value
    else:
        return "msgid not found"



def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def add_word(input_text):

    pattern = r'msgid "(.*?)"\nmsgstr "(.*?)"'
    match = re.search(pattern, input_text)
    if match:
        msgid_value = match.group(1)
        msgstr_value = match.group(2)
        new_msgstr_value = f'"{msgstr_value} слово"'
        updated_text = re.sub(pattern, fr'msgid "{msgid_value}"\nmsgstr "{new_msgstr_value}"', input_text)
        print(updated_text)
    else:
        print("msgid and msgstr not found")


input_text = '''
#: templates/components/index.html:406
msgid ""
"Дизайн современного кабинета для руководителя. Наша команда дизайнеров взяла "
"на себя задачу создаьб рабочее пространство, которое сочетает в себе "
"элегантный дизайн и практичность"
msgstr ""


#: templates/base.html:94 templates/components/index.html:101
msgid "Товары"
msgstr ""

#: templates/base.html:97 templates/components/index.html:104
#: templates/components/index.html:681
msgid "Продукция"
msgstr ""

#: templates/base.html:108 templates/components/index.html:115
#: templates/components/solutions.html:11
#: templates/components/solutions.html:14
#: templates/components/solutions.html:69
msgid "Решения"
msgstr ""

#: templates/base.html:113 templates/blog/designer-details.html:90
#: templates/blog/designers-grid.html:11 templates/components/index.html:120
msgid "Дизайнеры"
msgstr ""
'''
def group_separator(input_text):
    pattern = r'\n\n'
    items = re.split(pattern, input_text.strip())

    translations = []
    for item in items:
        match = re.search(r'#:.*?\nmsgid "(.*?)"\nmsgstr "(.*?)"', item)
        if match:
            translation = f"#:{match.group(0)}"
            translations.append(translation)
    return translations



texts = group_separator(input_text=input_text)
for i in texts:
    word = find_word(i)
    word_translate = translate_text(word)
    print(word_translate)
