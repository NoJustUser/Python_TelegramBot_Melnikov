import os.path


def read_note():
    try:
        note_ = input('Введите название заметки : ')
        note_name = note_ + '.txt'
        if os.path.isfile(note_name):
            with open(note_name, 'r', encoding='utf-8') as file:
                data = file.read()
            print(data)
            return note_
        print('Заметка не найдена.')
        return False
    except:
        print('Произошла ошибка.')
