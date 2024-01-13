import os.path


def delete_note():
    note_ = input('Введите название заметки : ')
    note_name = note_ + '.txt'
    if os.path.isfile(note_name):
        os.remove(note_name)
        print('Заметка успешно удалена.')
        return True
    print('Заметка не найдена.')
    return False

