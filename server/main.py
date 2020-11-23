import sys, time
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton, InputFile

from keyboard import Keyboard
from message import Message

handler = Message()
token = open("../config/token.txt", "r")
TOKEN = token.read()
bot = telegram.Bot(TOKEN)
f = open("../config/welcome.txt", "r")
welcome = f.read()
key = Keyboard()

# Push into que last update recived from user
def last_update():
    response = bot.getUpdates()
    last = len(response) - 1
    handler.setMessage(response[last])

def main():
    #update_id = last_update() + 1
    try:
        key.initData()
        print('You can start to use your bot')
        last_update()
        update_id = handler.getUpdateId() + 1
        while True:
            update = handler.getUpdateId()
            if  update == update_id:
                if handler.getMessage() == '/start':
                    key.send_message(bot, handler.getChatId(), welcome)
                    key.firstKeyboard(bot, handler.getChatId())
                elif handler.getMessage() == 'Back':
                    key.firstKeyboard(bot, handler.getChatId())  
                elif handler.getMessage() == 'Tracking':
                    key.sendRecap(bot, handler.getChatId())
                elif handler.getMessage() == 'Analysis':
                    key.analysisKeyboard(bot, handler.getChatId())   
                elif handler.getMessage() == 'Markowitz':
                    key.sendMarkowitz(bot, handler.getChatId())
                elif handler.getMessage() == 'Forecast':
                    key.sendForecast(bot, handler.getChatId())
                elif handler.getMessage() == 'CAPM':
                    key.sendCAPM(bot, handler.getChatId())     
                else:
                    key.send_message(bot, handler.getChatId(), "Sorry, this function is not available yet!")
                update_id += 1
                handler.move()
            last_update()
    except KeyboardInterrupt:
        pass
    

main()