import telegram
import sys
import os
from MC_Simulation import *
from capm import *
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
        btn1 = KeyboardButton(text = 'Tracking')
        btn2 = KeyboardButton(text = 'Analysis')
        btn3 = KeyboardButton(text = 'Forecast')
        btn4 = KeyboardButton(text = 'Help')
        keyboard = [[btn1, btn2, btn3, btn4]]
        self.send_keyboard(bot, keyboard, chat_id, '<strong>Menu</strong>')

    def analysisKeyboard(self, bot, chat_id):
        btn1 = KeyboardButton(text = 'Markowitz')
        btn2 = KeyboardButton(text = 'CAPM')
        btn3 = KeyboardButton(text = 'Back')
        keyboard = [[btn1, btn2, btn3]]
        self.send_keyboard(bot, keyboard, chat_id, '<strong>Portfolio Analysis</strong>')        

    def sendRecap(self, bot, chat_id):
        annualReturnW, volatility, amount = stock.recapPortfolio()
        self.sendImage(bot, chat_id, 'recap.png')
        message = ''
        message += ('The annual <u>return</u> of the portfolio is: ' + str(round(annualReturnW, 3)) + '%\n' + 'The <u>volatility</u> of the porfolio is: ' + str( round( (volatility*100), 2) ) + '%\n' + 'The <u>amount</u> of your portfolio is: ' + str( round(amount, 2) ) + '$\n')
        self.send_message(bot, chat_id, message)    
        annual_returns, tickers = stock.recapStock()
        message = ''
        for i in range(len(annual_returns)):
            message += ('The single annual return of the stock ' + '<u>' +tickers[i] + '</u>' +' is ' + \
                str( round(annual_returns.get(i)*100, 2) ) + '%\n' )
        self.sendImage(bot, chat_id, 'stock.png')
        self.send_message(bot, chat_id, message)

    def sendMarkowitz(self, bot, chat_id):
        pfpuntoMaxRet, pfpuntoMinVol, pfpuntoSharpe, tickers = stock.markovitz()
        self.sendImage(bot, chat_id, 'frontier.png')
        message = 'The porfolio with <u>maximum return</u> is combosed by:\n'
        for i in range( len(pfpuntoMaxRet.get('weig_list') ) ):
            message += ('Stock ticker: ' + tickers[i] + ' ' + str( round(pfpuntoMaxRet.get('weig_list')[i]*100, 2) ) + '%\n')
        message +=  ('\n<strong>Return:</strong> ' + str( round( pfpuntoMaxRet.get('Return')*100, 2) ) + '%\n' )  
        message +=  ('<strong>Volatility:</strong> ' + str( round( pfpuntoMaxRet.get('Volatility')*100, 2) ) + '%\n' )     
        message += ('<strong>Sharpe ratio is:</strong> ' + str( round(pfpuntoMaxRet.get('sharpe'), 2) ))
        self.send_message(bot, chat_id, message) 

        message = 'The porfolio with <u>minimum volatility</u> is combosed by:\n'
        for i in range( len(pfpuntoMinVol.get('weig_list') ) ):
            message += ('Stock ticker: ' + tickers[i] + ' ' + str( round(pfpuntoMinVol.get('weig_list')[i]*100, 2) ) + '%\n')
        message +=  ('\n<strong>Return:</strong> ' + str( round( pfpuntoMinVol.get('Return')*100, 2) ) + '%\n' )  
        message +=  ('<strong>Volatility:</strong> ' + str( round( pfpuntoMinVol.get('Volatility')*100, 2) ) + '%\n' )
        message += ('<strong>Sharpe ratio is:</strong> ' + str( round(pfpuntoMinVol.get('sharpe'), 2) ))
        self.send_message(bot, chat_id, message)

        message = 'The porfolio with <u>highest Sharpe ratio</u> is combosed by:\n'
        for i in range( len(pfpuntoSharpe.get('weig_list') ) ):
            message += ('Stock ticker: ' + tickers[i] + ' ' + str( round(pfpuntoSharpe.get('weig_list')[i]*100, 2) ) + '%\n')
        message +=  ('\n<strong>Return:</strong> ' + str( round( pfpuntoSharpe.get('Return')*100, 2) ) + '%\n' )  
        message +=  ('<strong>Volatility:</strong> ' + str( round( pfpuntoSharpe.get('Volatility')*100, 2) ) + '%\n' )
        message += ('<strong>Sharpe ratio is:</strong> ' + str( round(pfpuntoSharpe.get('sharpe'), 2) ))
        self.send_message(bot, chat_id, message)
 
    def sendForecast(self, bot, chat_id):
        mydata = stock.getMydata()
        avg, maxVal, minVal, stdVal = MC_Simulation(mydata)
        self.sendImage(bot, chat_id, 'mc_sim.png')
        message = 'Here there are five possible annually forecasts of the portfolio starting from one year ago with a capital amount of 10k $\n'
        message += ('\nThe <u>average</u> value of the prevision is: ' + str(avg) + '$')
        message += ('\nThe <u>maximum</u> value of the prevision is: ' + str(maxVal) + '$')
        message += ('\nThe <u>minimum</u> value of the prevision is: ' + str(minVal) + '$')
        self.send_message(bot, chat_id, message)
        
    def sendCAPM(self, bot, chat_id):
        pfpuntoMaxRet, pfpuntoMinVol, pfpuntoSharpe, tickers = stock.markovitz()
        weights = pfpuntoMinVol.get('weig_list')
        mydata = stock.getMydata()
        SP500_ret = stock.getSP500()
        yr_10 = stock.getYR10()
        #weights = stock.getWeights()
        alpha, beta, sharpe = CAPM(mydata, stock, weights, SP500_ret, yr_10)
        self.sendImage(bot, chat_id, 'capm.png')
        message = ('Your portfolio excess return vaires by (beta) ' + str( round(beta, 2) )  + ' as the Market Excess Return Increases by one unit \nYour portfolio is overperfoming/underperforming the benchmark by (alpha)' + str( round(alpha, 2) ) + '\nYour porfolio has performed with this Sharpe ratio: ' + str(round(sharpe, 2)) )
        self.send_message(bot, chat_id, message)

    def sendImage(self, bot, chat_id, img):
        image = '../img/' + img
        bot.sendPhoto(chat_id, photo=open(image, 'rb'))

    def send_keyboard(self, bot, keyboard, chat_id, text_message):
        bot.sendMessage(chat_id, text = text_message, parse_mode='HTML', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))

    def send_message(self, bot, chat_id, text_message):
        bot.sendMessage(chat_id, text = text_message, parse_mode='HTML')