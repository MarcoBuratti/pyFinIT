import json
import sys, time
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton, InputFile
from keyboard import firstKeyboard, analysisKeyboard, sendImage, send_message

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

def main():
    update_id = last_update() + 1
    try:
        while True:
            #time.sleep(3)
            update = last_update()
            if update_id == update:
                if get_message_text() == '/start' or get_message_text() == '/back':
                    firstKeyboard(bot, get_chat_id())  
                elif get_message_text() == 'Analysis':
                    analysisKeyboard(bot, get_chat_id())   
                elif get_message_text() == 'Recap':
                      sendImage(bot, get_chat_id())
                else:
                    send_message(bot, get_chat_id(), get_message_text())
                update_id += 1
    except KeyboardInterrupt:
        pass
    

main()