import telebot
import config
import wikipedia

from telebot import types

wikipedia.set_lang("ru")

client = telebot.TeleBot(config.TOKEN)

@client.message_handler(commands = ['start'])
def hello(message):
    sti = open('static/welcome.webp', 'rb')
    client.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📱Поиск информации📱")
    item2 = types.KeyboardButton("❗️О сетке ботов inedubots❗️")
    item3 = types.KeyboardButton("💸Поддержать💸")
    item4 = types.KeyboardButton("🔴Русский язык поиска🔴")
    item5 = types.KeyboardButton("🟠Английский язык поиска🟠")

    markup.add(item1, item2, item3, item4, item5)

    client.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный MIKHAN_GO для поиска информации в википедии)".format(message.from_user, 
    client.get_me()), parse_mode='html', reply_markup=markup)


@client.message_handler(content_types = ['text'])
def answer(message):
    if message.text == "📱Поиск информации📱":

        client.send_message(message.chat.id, "🔍Введите запрос для поиска🔍")

    elif message.text == "❗️О сетке ботов inedubots❗️":

        client.send_message(message.chat.id, "❗️Сетка ботов inedubots создана для привлечения инвестиций к боту @RuHelpEducationBot❗️")
        client.send_message(message.chat.id, "❗️В сетку ботов входят боты: @rubdollarbot, @pernamebot, @wikiinedubot, @mathinedubot❗️")

    elif message.text == "💸Поддержать💸":

        client.send_message(message.chat.id, "💎5599 0050 4579 2269💎")

    elif message.text == "🔴Русский язык поиска🔴":

        client.send_message(message.chat.id, "🔴Установлено🔴")
        wikipedia.set_lang("ru")

    elif message.text == "🟠Английский язык поиска🟠":

        client.send_message(message.chat.id, "🟠Установлено🟠")
        wikipedia.set_lang("en")

    elif message.text != "📱Поиск информации📱" or "💸Поддержать💸" or "❗️О сетке ботов inedubots❗️":
        try:
            client.send_message(message.chat.id, "Вот результат поиска вашего запроса в википедии: " + wikipedia.summary(message.text))
        except ConnectionError:
            client.send_message(message.chat.id, "🔴Смените язык🔴")
        except:
            client.send_message(message.chat.id, "🔴Несуществующий запрос!🔴")

client.polling(none_stop = True, interval = 0)