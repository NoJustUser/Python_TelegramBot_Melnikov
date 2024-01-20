from build_note import build_note


def create_note():
    try:
        note_name = input('Введите название заметки : ')
        note_text = input('Введите текст заметки : ')
        build_note(note_text, note_name)
    except:
        print('Произошла ошибка.')
