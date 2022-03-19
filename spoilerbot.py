import telebot
from telebot import types
from telebot import util

bot = telebot.TeleBot("5204902361:AAHezIn8IjmOw1frFjohfjwqxARYcHfUr4E", parse_mode=None)

@bot.message_handler(commands=['start', 'spoiler'])
def start(message):
    bot.send_message(message.chat.id,
                     'Hi! Send me a text and I will convert it into the new spoiler formatting! You can try using me with inline mode as well!\nLearn more: /help')

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, 'Send any text to me and I will return you the text in spoiler formatting like this: <tg-spoiler>Hello!</tg-spoiler>\n\nYou can use me in inline mode as well! Type @spoilerbot in the message field and type anything. Tap on the pop-up and you will get the text in spoiler formatting! \n\nPlease make sure that you have updated Telegram to the latest version. \n\n\nDeveloped by @whbots', parse_mode='HTML')

@bot.message_handler(content_types='text')
def receive(m):
    getmsg = m.text
    bot.send_message(m.chat.id, f'<tg-spoiler>{getmsg}</tg-spoiler>', parse_mode = 'HTML')

@bot.inline_handler(lambda query: query)
def querytext(inline_query):
    r = types.InlineQueryResultArticle('1', thumb_url='http://telegramfiles.com/files/12159634/01e6f991771249a0b31703dc8d9b04ad/image_2022-03-02_10-32-43.png',title=f"Tap to send '{inline_query.query}' as spoiler", description=f'||{inline_query.query}||', input_message_content=types.InputTextMessageContent(f'<tg-spoiler>{inline_query.query}</tg-spoiler>', parse_mode = 'HTML'))
    bot.answer_inline_query(inline_query.id, [r])

bot.infinity_polling()