# from tokenize import Token
# import telebot
# from googletrans import Translator

# translator = Translator()
# Token = '5596294851:AAGlFO8eG33ERXrca6dYyQ6urUknWsgKUdI'

# bot = telebot.TeleBot(token = Token)

# @bot.message_handler(commands = ['start'])
# def sendmessage(message):
#     username = message.chat.first_name
#     bot.send_message(message.chat.id, 'Yello')

# @bot.message_handler(content_types = 'text')
# def sentmess(message):
#     cl_message = translator.translate(message.text, dest = 'ru').text
#     print(message.text)
#     bot.send_message(message.chat.id, cl_message)


    
# bot.infinity_polling()