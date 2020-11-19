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
    annual_returns, annualReturnW, volatility, tickers = stock.recapKey()
    send_message(bot, chat_id, 'The annual return of the portfolio is: ' + str(round(annualReturnW, 3)) + '%\n' \
        + 'The volatility of the porfolio is: ' + str( round( (volatility*100), 2) ) + '%\n')
    message = ''
    for i in range(len(annual_returns)):
        message += ('The single annual return of the stock ' + tickers[i] + ' is ' +\
             str( round(annual_returns.get(i)*100, 2) ) + '%\n' )
    send_message(bot, chat_id, message)

def sendImage(bot, chat_id, img):
    image = '../img/' + img
    bot.sendPhoto(chat_id, photo=open(image, 'rb'))


def send_keyboard(bot, keyboard, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message, parse_mode='HTML', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))

def send_message(bot, chat_id, text_message):
    bot.sendMessage(chat_id, text = text_message, parse_mode='HTML')