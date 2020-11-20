import telegram
import sys
sys.path.insert(1, '../Luca')
from stock import Stock
from telegram import ReplyKeyboardMarkup, KeyboardButton

stock = Stock()
##### Class in which we manage the user's keyboard
class Keyboard:

    def __init__(self):
        self.mess = None        

    def initData(self):
        print('Initialize Data')
        stock.initData()

    def firstKeyboard(self, bot, chat_id):
        btn1 = KeyboardButton(text = 'Recap')
        btn2 = KeyboardButton(text = 'Analysis')
        btn3 = KeyboardButton(text = 'Forecast')
        keyboard = [[btn1, btn2, btn3]]
        self.send_keyboard(bot, keyboard, chat_id, '<strong>Menu</strong>')

    def analysisKeyboard(self, bot, chat_id):
        btn1 = KeyboardButton(text = 'Markowitz')
        btn2 = KeyboardButton(text = 'CAPM')
        keyboard = [[btn1, btn2]]
        self.send_keyboard(bot, keyboard, chat_id, '<strong>Portfolio Analysis</strong>')        

    def sendRecap(self, bot, chat_id):
        annual_returns, annualReturnW, volatility, tickers = stock.recapKey()
        message = ''
        for i in range(len(annual_returns)):
            message += ('The single annual return of the stock ' + tickers[i] + ' is ' + \
                str( round(annual_returns.get(i)*100, 2) ) + '%\n' )
        self.send_message(bot, chat_id, message)
        self.sendImage(bot, chat_id, 'stockRecap.png')
        self.send_message(bot, chat_id, 'The annual return of the portfolio is: ' + str(round(annualReturnW, 3)) + '%\n' \
            + 'The volatility of the porfolio is: ' + str( round( (volatility*100), 2) ) + '%\n')
        
    def sendMarkowitz(self, bot, chat_id):
        pfpuntoMaxRet, pfpuntoMinVol = stock.markovitz()
        #print(type(pfpuntoMaxRet.get('weig_list')))
        #print(pfpuntoMaxRet.get('weig_list'))
        self.sendImage(bot, chat_id, 'frontier.png')
        self.send_message(bot, chat_id, str(pfpuntoMaxRet)) 
        self.send_message(bot, chat_id, str(pfpuntoMinVol))  
        
    def sendImage(self, bot, chat_id, img):
        image = '../img/' + img
        bot.sendPhoto(chat_id, photo=open(image, 'rb'))


    def send_keyboard(self, bot, keyboard, chat_id, text_message):
        bot.sendMessage(chat_id, text = text_message, parse_mode='HTML', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))

    def send_message(self, bot, chat_id, text_message):
        bot.sendMessage(chat_id, text = text_message, parse_mode='HTML')