from read_note import read_note
from build_note import build_note


def edit_note():
    try:
        note_name = read_note()
        if note_name:
            note_text = input('Введите текст заметки для обновления : ')
            build_note(note_text, note_name)
            return True
        print('Заметка не найдена.')
        return False
    except:
        print('Произошла ошибка.')
