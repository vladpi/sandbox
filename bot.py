import os

import telebot
import wikipedia
from dotenv import load_dotenv
from telebot import types

load_dotenv()
client = telebot.TeleBot(os.getenv('BOT_TOKEN'))

SEARCH_BUTTON = '📱Поиск информации📱'
ABOUT_BUTTON = '❗️О сетке ботов inedubots❗️'
SUPPORT_BUTTON = '💸Поддержать💸'
RUS_BUTTON = '🔴Русский язык поиска🔴'
ENG_BUTTON = '🟠Английский язык поиска🟠'

HELLO_MESSAGE = 'Добро пожаловать, {0.first_name}!\n' \
                'Я - <b>{1.first_name}</b>, бот созданный MIKHAN_GO для поиска информации в википедии)'
ENTER_QUERY_MESSAGE = '🔍Введите запрос для поиска🔍'
CHANGE_LANGUAGE_MESSAGE = '🔴Смените язык🔴'
BAD_WIKI_REQUEST_MESSAGE = '🔴Такого запроса нету в википедии!🔴'
ABOUT_MESSAGE = '❗️В сетку ботов входят боты: @rubdollarbot, @pernamebot, @wikiinedubot, @mathinedubot❗️\n' \
                '❗️Сетка ботов inedubots создана для привлечения инвестиций к боту @RuHelpEducationBot❗️'
CARD_NUMBER_MESSAGE = '💎5599 0050 4579 2269💎'
RED_SET_MESSAGE = '🔴Установлено🔴'
ORANGE_SET_MESSAGE = '🟠Установлено🟠'
BAD_REQUEST_MESSAGE = '🔴Несуществущий запрос!🔴'


@client.message_handler(commands=['start'])
def start_handler(message):
    # hello = open('static/welcome.webp', 'rb')
    # client.send_sticker(message.chat.id, hello)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton(SEARCH_BUTTON),
        types.KeyboardButton(ABOUT_BUTTON),
        types.KeyboardButton(SUPPORT_BUTTON),
        types.KeyboardButton(RUS_BUTTON),
        types.KeyboardButton(ENG_BUTTON),
    )

    client.send_message(
        message.chat.id,
        HELLO_MESSAGE.format(message.from_user, client.get_me()),
        parse_mode='html',
        reply_markup=markup,
    )


@client.message_handler(regexp=SEARCH_BUTTON)
def start_search_handler(message):
    client.send_message(message.chat.id, ENTER_QUERY_MESSAGE)
    client.register_next_step_handler(message, search_query_handler)


def search_query_handler(message):
    try:
        client.send_message(
            message.chat.id,
            'Вот результат поиска вашего запроса в википедии: '
            + wikipedia.summary(message.text),
        )

    except ConnectionError:
        client.send_message(message.chat.id, CHANGE_LANGUAGE_MESSAGE)

    except:
        client.send_message(message.chat.id, BAD_WIKI_REQUEST_MESSAGE)


@client.message_handler(regexp=ABOUT_BUTTON)
def about_handler(message):
    client.send_message(message.chat.id, ABOUT_MESSAGE)


@client.message_handler(regexp=SUPPORT_BUTTON)
def support_handler(message):
    client.send_message(message.chat.id, CARD_NUMBER_MESSAGE)


@client.message_handler(regexp=RUS_BUTTON)
def rus_handler(message):
    client.send_message(message.chat.id, RED_SET_MESSAGE)
    wikipedia.set_lang('ru')


@client.message_handler(regexp=ENG_BUTTON)
def eng_handler(message):
    client.send_message(message.chat.id, ORANGE_SET_MESSAGE)
    wikipedia.set_lang('en')


@client.message_handler(content_types=['text'])
def fallback(message):
    client.send_message(message.chat.id, BAD_REQUEST_MESSAGE)


if __name__ == '__main__':
    wikipedia.set_lang('ru')
    client.polling(none_stop=True, interval=0)
