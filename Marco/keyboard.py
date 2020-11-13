import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton

##### Class in which we manage the user's keyboard


def firstKeyboard(bot, chat_id):
    btn1 = KeyboardButton(text = 'Recap')
    btn2 = KeyboardButton(text = 'Analysis')
    btn3 = KeyboardButton(text = 'Forecast')
    keyboard = [[btn1, btn2, btn3]]
    send_keyboard(bot, keyboard, chat_id, '<strong>Menu</strong>')

def analysisKeyboard(bot, chat_id):
    btn1 = KeyboardButton(text = 'Markovitz')
    btn2 = KeyboardButton(text = 'CAPM')
    btn3 = KeyboardButton(text = 'Non capisco')
    keyboard = [[btn1, btn2, btn3]]
    send_keyboard(bot, keyboard, chat_id, '<strong>Portfolio Analysis</strong>')        

"""
def sendShortCut(bot):
    cmd1 = BotCommand(command='/start', description='Start the Bot')
    cmd2 = BotCommand(command='/help', description='Ask for help to the Bot')
    cmd3 = BotCommand(command='/exit', description='Reset the Keyboard')
    cmd4 = BotCommand(command='/back', description='Back to the starting keyboard')
    command = [[cmd1, cmd2, cmd3, cmd4]]
    bot.setMyCommands(command)
"""

def sendImage(bot, chat_id):
    bot.sendPhoto(chat_id, photo=open('../img/stock.png', 'rb'))


def send_keyboard(bot, keyboard, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message, parse_mode='HTML', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))

def send_message(bot, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message)