import os.path


def read_note(note_n):
    note_name = note_n + '.txt'
    if os.path.isfile(note_name):
        with open(note_name, 'r', encoding='utf-8') as file:
            data = file.read()
        return 'Текст заметки:\n' + data
    return 'Заметка не найдена.'
