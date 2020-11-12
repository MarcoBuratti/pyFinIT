import json
import sys, time
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton, InputFile
from keyboard import firstKeyboard, analysisKeyboard, backKeyboard

TOKEN = '1406935640:AAE3-CXn5zEgvB-xdBQw67zA2bo7r0TGCDE'

bot = telegram.Bot(TOKEN)

# Return last update_id
def last_update():
    response = bot.getUpdates()
    last = len(response) - 1
    #print(response[last]['update_id'])
    return response[last]['update_id']

# Return the chat id
def get_chat_id():
    response = bot.getUpdates()
    last = len(response) - 1
    chat_id = response[last]['message']['chat']['id']
    return chat_id

# Return the message send by the client
def get_message_text():
    response = bot.getUpdates()
    last = len(response) - 1
    message_text = response[last]['message']['text']
    return message_text    


# Send message from serverbot to chat
def send_message(chat_id, message_text):
    bot.sendMessage(chat_id, message_text)

# Send keyboard to user
def send_keyboard():
    btn1 = KeyboardButton(text = 'AMZN')
    btn2 = KeyboardButton(text = 'AAPL')
    keyboard = [[btn1, btn2]]
    bot.sendMessage(get_chat_id(), text = 'Stocks', reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True))

def main():
    update_id = last_update() + 1
    try:
        while True:
            #time.sleep(3)
            update = last_update()
            if update_id == update:
                if get_message_text() == '/start':
                    firstKeyboard(bot, get_chat_id())
                elif get_message_text() == 'Back':
                    backKeyboard(bot, get_chat_id())     
                elif get_message_text() == 'Analysis':
                    analysisKeyboard(bot, get_chat_id())   
                elif get_message_text() == 'Recap':
                    bot.sendPhoto(get_chat_id(), photo=open('../Marco/stock.png', 'rb'))  
                update_id += 1
    except KeyboardInterrupt:
        pass
    

main()