import os.path


def display_notes():
    files = os.listdir()
    len_dict = {}
    list_notes = [file for file in files if file.endswith('.txt')]

    for note in list_notes:
        with open(note, 'r') as file:
            text = file.read()
        len_dict[text] = len(text)

    res = sorted(len_dict.items(), key=lambda x: x[1])
    for text, len_text in res:
        print(text)

