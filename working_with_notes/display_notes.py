import os.path


def display_notes():
    s = input('Хотите вывести заметки по убыванию (да/нет) ? ')
    flag = False if s == 'нет' else True
    files = os.listdir()
    len_dict = {}
    list_notes = [file for file in files if file.endswith('.txt')]

    for note in list_notes:
        with open(note, 'r') as file:
            text = file.read()
        len_dict[text] = len(text)

    # Сортируем список кортежей по второму элементу (значению для len_dict)
    res = sorted(len_dict.items(), key=lambda x: x[1], reverse=flag)
    for text, len_text in res:
        print(text)

