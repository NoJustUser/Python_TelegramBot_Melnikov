from create_note import create_note
from read_note import read_note
from edit_note import edit_note
from delete_note import delete_note
from display_notes import display_notes

options_for_action = {
    '1': [' - Создать заметку', 'create_note'],
    '2': [' - Прочитать заметку', 'read_note'],
    '3': [' - Отредактировать заметку', 'edit_note'],
    '4': [' - Удалить заметку', 'delete_note'],
    '5': [' - Вывести список заметок', 'display_notes'],
    '6': [' - Выход из программы'],
}
print('Выберите необходимый вариант действий :')
for key, value in options_for_action.items():
    print('\t\t', key, value[0])

while True:
    try:
        key = input('Выберите необходимое действие : ')
        if key == '6':
            print('Вы вышли из программы.')
            break
        func = options_for_action.get(key)[1]
        eval(f'{func}()')
    except:
        print('Произошла ошибка.')
        break
