from telegram import bot

import secrets
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from create_note import create_note
from delete_note import delete_note
from edit_note import edit_note
from display_notes import display_notes
from read_note import read_note

options_for_action = {
    '/create': [' - Создать заметку', create_note,
                'Для создания заметки в 1-м сообщении введите название заметки, во 2-м ее текст',
                'Текст заметки: '],
    '/delete': [' - Удалить заметку', delete_note,
                'Чтобы удалить заметку введите ее название',
                'Название заметки: '],
    '/read': [' - Прочитать заметку', read_note,
              'Чтобы прочитать заметку введите ее название',
              'Название заметки: '],
    '/edit': [' - Редактировать заметку', edit_note,
              'Для редактирования заметки введите ее название \n Я покажу вам ее содежимое. \nПосле этого введите новый'
              'текст заметки', 'Текст заметки: '],
    '/display': [' - Показать все заметки', display_notes, 'Вывести заметки по убыванию их длины (да/нет) ?',
                 'Вот отсортированный список: '],
}

updater = Updater(token=secrets.API_TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'Привет, Я Бот !\nИ я могу предложить Вам поработать с заметками. \nВот что я могу '
                                  f'предложить :')
    # Вывод всех доступных опций для действий с заметками
    msg = []
    for key, value in options_for_action.items():
        msg.append(f'{key} {value[0]} \n')
    context.bot.send_message(chat_id=update.effective_chat.id, text=''.join(msg))


# data - для сохранения переменных note_text / note_name (текст заметки / название заметки)
# или флаг s (да/нет) для функции display_notes. Временное хранилище данных
data = []
command = []  # Хранилище данных последней команды, которую использовал пользователь


def get_user_action(update, context):
    try:
        data.append(update.message.text)
        if command[0] in ['/create', '/edit']:
            # Если команда /edit сначала читаем файл и выводим содержимое
            if command[0] == '/edit' and len(data) == 1:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=read_note(data[0]))
            if len(data) > 1:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Название заметки: ' + data[0] + '\n'
                                         + options_for_action.get(command[0])[3] + data[1])
                note_name, note_text = data[0], data[1]
                func = options_for_action.get(command[0])[1]
                text = func(note_name, note_text)
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=text)
                del command[:]
        else:
            tmp = data[0] if command[0] != '/display' else ''
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=options_for_action.get(command[0])[3] + tmp)
            note_name = data[0]
            func = options_for_action.get(command[0])[1]
            text = func(note_name)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=text)
            del command[:]
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


def make_note_handler(update, context):
    tmp = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=options_for_action.get(tmp)[2])
    try:
        # очистка кэша (старые данные)
        del data[:]
        del command[:]
        # сохраняем название команды
        command.append(update.message.text)
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


# регистрация обработчика ввода команд для действий с заметками
for key, value in options_for_action.items():
    dispatcher.add_handler(CommandHandler(key[1:], make_note_handler))
    # dispatcher.add_handler(CommandHandler(key[1:], value[1]))

# регистрация обработчика команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# регистрация обработчика ввода текстовых сообщений от пользователя
get_message = MessageHandler(Filters.text, get_user_action)
dispatcher.add_handler(get_message)

updater.start_polling()
