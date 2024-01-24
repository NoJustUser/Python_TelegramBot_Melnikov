
def edit_note(note_name, note_text):
    if note_name:
        note_name = note_name + '.txt'
        with open(f'{note_name}', 'w', encoding='utf-8') as file:
            file.write(note_text)
        return f'Заметка {note_name[:-4]} отредактирована и сохранена.'
    return 'Заметка не найдена.'
