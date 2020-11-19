import json

class Message:

    def __init__(self):
        self.chat_id = None
        self.text = None
        self.update_id = None
        self.first_name = None
        self.last_name = None

    def setMessage(self, response):
        self.chat_id = response['message']['chat']['id']
        self.text = response['message']['text']
        self.update_id = response['update_id']
        self.first_name = response['message']['chat']['first_name']
        self.last_name = response['message']['chat']['last_name']

    # Return update_id from last message
    def getUpdateId(self):
        return self.update_id

    # Return the message send by the client
    def getMessage(self):
        return self.text

    # Return the chat id
    def getChatId(self):
        return self.chat_id
    
    def getName(self):
        return self.first_name

    def getSurname(self):
        return self.last_name

    def move(self):
        print('User: ', self.getName(), ' ', self.getSurname(), ' has request this function: ', self.getMessage())
