import sys, time
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton, InputFile

from keyboard import *
from message import Message

handler = Message()
token = open("../config/token.txt", "r")
TOKEN = token.read()
bot = telegram.Bot(TOKEN)
f = open("../config/welcome.txt", "r")
welcome = f.read()

# Push into que last update recived from user
def last_update():
    response = bot.getUpdates()
    last = len(response) - 1
    handler.setMessage(response[last])

def main():
    #update_id = last_update() + 1
    try:
        last_update()
        update_id = handler.getUpdateId() + 1
        while True:
            time.sleep(0.2)
            update = handler.getUpdateId()
            if  update == update_id:
                if handler.getMessage() == '/start':
                    send_message(bot, handler.getChatId(), welcome)
                    firstKeyboard(bot, handler.getChatId())
                elif handler.getMessage() == '/back':
                    firstKeyboard(bot, handler.getChatId())  
                elif handler.getMessage() == 'Analysis':
                    analysisKeyboard(bot, handler.getChatId())   
                elif handler.getMessage() == 'Recap':
                    sendImage(bot, handler.getChatId())
                else:
                    send_message(bot, handler.getChatId(), "Sorry, this function is not available yet!")
                update_id += 1
            last_update()
    except KeyboardInterrupt:
        pass
    

main()