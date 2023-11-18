import telebot
from random import randint
bot = telebot.TeleBot('5633178978:AAEdi_Yn3rd94sYcSLNPYTcJAzDGbYub8ps')


@bot.message_handler(commands= ['start'])
def start(message):
    mess = f'<b>Hello</b>, {message.from_user.first_name}({message.from_user.username}) '
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user(message):
    hui = f'{randint(0, 25)} см, неплохо. но у абика все равно больше' 
    if message.text == 'хуй':
        bot.send_message(message.chat.id, hui )
    elif message.text == '❤️':
        bot.send_message(message.chat.id, 'ты ж моя любимка❤️❤️❤️❤️❤️' )
    elif message.text == 'севара':
        bot.send_message(message.chat.id, 'жду когда ее выебу' )
    elif message.text == 'фото':
        photo  = open('media/pachita1.jpeg', 'rb')
        photo2 = open('media/pachita2.jpeg', 'rb')
        photo3 = open('media/pachita3.jpeg', 'rb')
        photo4 = open('media/pachita4.jpeg', 'rb')
        bot.send_message(message.chat.id, 'держи пачиту')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo2)
        bot.send_photo(message.chat.id, photo3)
        bot.send_photo(message.chat.id, photo4)
    else:
        bot.send_message(message.chat.id, 'че' )

@bot.message_handler(content_types=['photo'])
def photo_user(message):
        bot.send_message(message.chat.id, 'мой создатель пока что, мне не разрешил смотреть нюдсы, тем более их сливать. но ты можешь мне просто их скидывать))' )









bot.polling(none_stop=True)
