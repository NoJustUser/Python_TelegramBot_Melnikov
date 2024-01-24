import os.path


def display_notes(s):
    if s in ['да', 'нет']:
        flag = False if s == 'нет' else True
    else:
        return 'Некорректный ввод.'
    files = os.listdir()
    len_dict = {}
    list_notes = [file for file in files if file.endswith('.txt')]

    for note in list_notes:
        with open(note, 'r') as file:
            text = file.read()
        len_dict['Название заметки: ' + note + '\n' + 'Текст заметки: ' + text] = len(text)

    # Сортируем список кортежей по второму элементу (значению для len_dict)
    res = sorted(len_dict.items(), key=lambda x: x[1], reverse=flag)
    res_list = []
    for text, len_text in res:
        res_list.append(text + '\n\n')
    return ''.join(res_list)
