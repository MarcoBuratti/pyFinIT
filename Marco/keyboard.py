import telegram
import sys
sys.path.insert(1, '../Luca')
from stock import Stock
from telegram import ReplyKeyboardMarkup, KeyboardButton

stock = Stock()
##### Class in which we manage the user's keyboard

def firstKeyboard(bot, chat_id):
    btn1 = KeyboardButton(text = 'Recap')
    btn2 = KeyboardButton(text = 'Analysis')
    btn3 = KeyboardButton(text = 'Forecast')
    keyboard = [[btn1, btn2, btn3]]
    send_keyboard(bot, keyboard, chat_id, '<strong>Menu</strong>')
    stock.initData()

def analysisKeyboard(bot, chat_id):
    btn1 = KeyboardButton(text = 'Markovitz')
    btn2 = KeyboardButton(text = 'CAPM')
    keyboard = [[btn1, btn2]]
    send_keyboard(bot, keyboard, chat_id, '<strong>Portfolio Analysis</strong>')        

def sendRecap(bot, chat_id):
    annual_returns, annualReturnW, volatility = recapKey()
    send_message(bot, chat_id, str(annual_returns) + '\n' + str(annualReturnW) + '\n' + str(volatility))
    #+ annualReturnW + volatility

def sendImage(bot, chat_id):
    bot.sendPhoto(chat_id, photo=open('../img/stock.png', 'rb'))


def send_keyboard(bot, keyboard, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message, parse_mode='HTML', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))

def send_message(bot, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message, parse_mode='HTML')