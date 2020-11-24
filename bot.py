# import нужных библиотек
import telebot
# import config
import wikipedia

from telebot import types

# объявляем переменные
search = "📱Поиск информации📱"
about = "❗️О сетке ботов inedubots❗️"
support = "💸Поддержать💸"
rus = "🔴Русский язык поиска🔴"
eng = "🟠Английский язык поиска🟠"
enter = "🔍Введите запрос для поиска🔍"
about_reaction = "❗️В сетку ботов входят боты: @rubdollarbot, @pernamebot, @wikiinedubot, @mathinedubot❗️ \n❗️Сетка ботов inedubots создана для привлечения инвестиций к боту @RuHelpEducationBot❗️"
diamond = "💎5599 0050 4579 2269💎"
set_red = "🔴Установлено🔴"
set_orange = "🟠Установлено🟠"

# устанавливаем русский язык поиска (по умолчанию)
wikipedia.set_lang("ru")

# берём токен из файла
client = telebot.TeleBot("1358011014:AAGa1B9724IRJhIxaiBKUYXKqwEpOkDC6ws")

# команда старта бота
@client.message_handler(commands = ['start'])
def hello(message):
    # отправляем стикер
    hello = open('static/welcome.webp', 'rb')
    client.send_sticker(message.chat.id, hello)

    # добавляем клавиатуру к сообщению
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search = types.KeyboardButton(search)
    about = types.KeyboardButton(about)
    support = types.KeyboardButton(support)
    rus = types.KeyboardButton(rus)
    eng = types.KeyboardButton(eng)

    markup.add(search, about, support, rus, eng)

    # отправляем сообщение с прикреплённой клавиатурой, приветствуя пользователя по никнейму
    client.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный MIKHAN_GO для поиска информации в википедии)".format(message.from_user,
    client.get_me()), parse_mode='html', reply_markup=markup)

def search_wikipedia(message):
    # выводим запрос поиска в википедии
    try:
        client.send_message(message.chat.id, "Вот результат поиска вашего запроса в википедии: " + wikipedia.summary(message.text))
    # иначе если ошибка подключения пишем о смене языка
    except ConnectionError:
        client.send_message(message.chat.id, "🔴Смените язык🔴")
    except:
        client.send_message(message.chat.id, "🔴Такого запроса нету в википедии!🔴")

# если всё хорошо
try:
    # search
    @client.message_handler(regexp=search)
    def search(message):
        client.send_message(message.chat.id, enter)
        client.register_next_step_handler(message, search_wikipedia)

    # about
    @client.message_handler(regexp=search)
    def about(message):
        client.send_message(message.chat.id, about_reaction)

    # support
    @client.message_handler(regexp=support)
    def about(message):
        client.send_message(message.chat.id, diamond)

    # rus
    @client.message_handler(regexp=search)
    def about(message):
        client.send_message(message.chat.id, set_red)
        wikipedia.set_lang("ru")

    #eng
    @client.message_handler(regexp=search)
    def about(message):
        client.send_message(message.chat.id, set_orange)
        wikipedia.set_lang("en")

except:
    client.send_message(message.chat.id, "🔴Несуществущий запрос!🔴")

# запускаем бота
client.polling(none_stop = True, interval = 0)