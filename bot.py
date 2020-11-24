# import нужных библиотек
import telebot
import config
import wikipedia

from telebot import types

# устанавливаем русский язык поиска (по умолчанию)
wikipedia.set_lang("ru")

# берём токен из файла
client = telebot.TeleBot(config.TOKEN)

# команда старта бота
@client.message_handler(commands = ['start'])
def hello(message):
    # отправляем стикер
    hello = open('static/welcome.webp', 'rb')
    client.send_sticker(message.chat.id, hello)

    # добавляем клавиатуру к сообщению
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search = types.KeyboardButton("📱Поиск информации📱")
    about = types.KeyboardButton("❗️О сетке ботов inedubots❗️")
    support = types.KeyboardButton("💸Поддержать💸")
    rus = types.KeyboardButton("🔴Русский язык поиска🔴")
    en = types.KeyboardButton("🟠Английский язык поиска🟠")

    markup.add(search, about, support, rus, en)

    # отправляем сообщение с прикреплённой клавиатурой, приветствуя пользователя по никнейму
    client.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный MIKHAN_GO для поиска информации в википедии)".format(message.from_user,
    client.get_me()), parse_mode='html', reply_markup=markup)


# реакция на остальные сообщения (не команды)
@client.message_handler(content_types = ['text'])
def answer(message):
    # проверяем текст сообщения

    # search
    if message.text == "📱Поиск информации📱":

        client.send_message(message.chat.id, "🔍Введите запрос для поиска🔍")

    # about
    elif message.text == "❗️О сетке ботов inedubots❗️":

        client.send_message(message.chat.id, "❗️Сетка ботов inedubots создана для привлечения инвестиций к боту @RuHelpEducationBot❗️")
        client.send_message(message.chat.id, "❗️В сетку ботов входят боты: @rubdollarbot, @pernamebot, @wikiinedubot, @mathinedubot❗️")

    # support
    elif message.text == "💸Поддержать💸":

        client.send_message(message.chat.id, "💎5599 0050 4579 2269💎")

    # rus
    elif message.text == "🔴Русский язык поиска🔴":

        client.send_message(message.chat.id, "🔴Установлено🔴")
        wikipedia.set_lang("ru")

    # en
    elif message.text == "🟠Английский язык поиска🟠":

        client.send_message(message.chat.id, "🟠Установлено🟠")
        wikipedia.set_lang("en")

    # иначе
    else:
        try:

            # либо выводим запрос поиска в википедии
            client.send_message(message.chat.id, "Вот результат поиска вашего запроса в википедии: " + wikipedia.summary(message.text))

        # иначе если ошибка подключения пишем о смене языка
        except ConnectionError:
            client.send_message(message.chat.id, "🔴Смените язык🔴")

        # в противном случае
        except:
            client.send_message(message.chat.id, "🔴Несуществующий запрос!🔴")

# запускаем бота
client.polling(none_stop = True, interval = 0)