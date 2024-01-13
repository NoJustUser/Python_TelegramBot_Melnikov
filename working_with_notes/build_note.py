def build_note(note_text, note_name):
    with open(f'{note_name}.txt', 'w', encoding='utf-8') as file:
        file.write(note_text)
    print(f'Заметка {note_name} создана.')

