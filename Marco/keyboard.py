import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
#from main import get_chat_id

BACK_KEY = 0

##### Class in which we manage the user's keyboard

def firstKeyboard(bot, chat_id):
    BACK_KEY = 0
    btn1 = KeyboardButton(text = 'Recap')
    btn2 = KeyboardButton(text = 'Analysis')
    btn3 = KeyboardButton(text = 'Back')
    keyboard = [[btn1, btn2, btn3]]
    send_keyboard(bot, keyboard, chat_id, '<strong>Menu</strong>')

def analysisKeyboard(bot, chat_id):
    BACK_KEY = 1
    btn1 = KeyboardButton(text = 'Markovitz')
    btn2 = KeyboardButton(text = 'CAPM')
    btn3 = KeyboardButton(text = 'Non capisco')
    btn4 = KeyboardButton(text = 'Back')
    keyboard = [[btn1, btn2, btn3, btn4]]
    send_keyboard(bot, keyboard, chat_id, '<strong>Portfolio Analysis</strong>')        


def backKeyboard(bot, chat_id):
    previousKey = BACK_KEY - 1
    if previousKey == 0:
        firstKeyboard(bot, chat_id)
    elif previousKey == 1:
        analysisKeyboard(bot, chat_id)


def send_keyboard(bot, keyboard, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message, parse_mode='HTML', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))
