import os.path


def delete_note(note_name):
    note_name = note_name + '.txt'
    if os.path.isfile(note_name):
        os.remove(note_name)
        return 'Заметка успешно удалена.'
    return 'Заметка не найдена.'
