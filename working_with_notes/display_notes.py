import os.path


def display_notes():
    files = os.listdir()
    list_notes = [file for file in files if file.endswith('.txt')]
    for note in list_notes:
        with open(note, 'r') as file:
            text = file.read()
        print(text)


display_notes()
