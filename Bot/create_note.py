import os.path


def create_note(note_name, note_text):
    note_name = note_name + '.txt'
    if os.path.isfile(note_name):
        return f'Заметка {note_name} уже существует.\nдля редактирования выберите /edit'
    with open(f'{note_name}', 'w', encoding='utf-8') as file:
        file.write(note_text)
    return f'Заметка {note_name[:-4]} создана.'

