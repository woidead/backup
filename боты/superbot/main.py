import telebot
from config import TOKEN
from telebot import types
from pytube import *

from googletrans import Translator
import os
bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(commands=['start']) #обработка какой-то команды
def start(message):
    chat_id = message.chat.id
    if message.from_user.last_name == None:
        mess = f'привет, <b> {message.from_user.first_name}</b>'
    else:
        mess = f'привет, <b> {message.from_user.first_name} {message.from_user.last_name}</b>'

    bot.send_message(chat_id, mess, parse_mode='html') #вывод первое значение это в какой чат отправлять, а второе то что отправить. и еще можно указать метод вывода

# @bot.message_handler(content_types=['text']) #обработка любого текста
# def getusertext(message):
#     chat_id = message.chat.id
#     if message.text == 'hello': #отслеживание конкретного текста
#         bot.send_message(chat_id, message, parse_mode='html') #вывод первое значение это в какой чат отправлять, а второе то что отправить. и еще можно указать метод вывода
#     elif message.text == 'id':
#         bot.send_message(chat_id, message.from_user.id, parse_mode='html') #вывод первое значение это в какой чат отправлять, а второе то что отправить. и еще можно указать метод вывода
#     elif message.text == 'photo':
#         photo = open('kazuha.png', 'rb')
#         bot.send_photo(chat_id, photo ) #отправка фото 
#     elif message.text == 'video':
#         video = open('maz.mp4', 'rb')
#         bot.send_video_note(chat_id, video )

@bot.message_handler(content_types=['photo']) #отслеживание фото 
def getuserphoto(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'nice photo')



@bot.message_handler(commands=['web'])  
def web(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('our site', url = 'https://youtu.be'))
    bot.send_message(chat_id, 'перейдите на сайт', reply_markup=markup)




@bot.message_handler(commands=['help'])  
def web(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # resize_keyboard=True подстройка под интерфейс разных устройств, row_width=1 сколько будет кнопок в одной кнопке
    website = types.KeyboardButton('/web')
    start = types.KeyboardButton('/start')
    transle = types.KeyboardButton('/translate')
    yt = types.KeyboardButton('/youtube')
    markup.add(website, start, transle, yt)
    bot.send_message(chat_id, 'нажмите на нужную кнопку', reply_markup=markup)

@bot.message_handler(commands=['translate'])
def trans(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'начните переводить слова, написав, ваш текст для перевода после команды /перевести' )
    bot.send_message(chat_id, ''' пока что возможно переводить с ру на англ и с англ на ру
    пример: /перевести привет, друг ''' )




@bot.message_handler()
def translate(message):
    chat_id = message.chat.id
    text = message.json['text'].replace('/перевести ', '')
    langdetect = translator.detect(text)
    if langdetect.lang == 'ru':
        if message.json['text'].startswith('/перевести') == True:
            translations = translator.translate(text, dest='en')
            transtext = f'{translations.origin}  ->  {translations.text}'
            bot.send_message(chat_id, transtext )
    elif langdetect.lang == 'en':
        if message.json['text'].startswith('/перевести') == True:
            translations = translator.translate(text, dest='ru')
            transtext = f'{translations.origin}  ->  {translations.text}'
            bot.send_message(chat_id, transtext )

@bot.message_handler()
def youtubenotification(message):
    chat_id = message.chat.id
    text = message.json['text']
    yt = YouTube(text)
    if text.startswith == 'https://www.youtube.com/' or  text.startswith == "https://www.youtu.be/":
        bot.send_message(chat_id, f'*загрузка видео начата*: *{yt.title}*\n'
                                        f'*С канала*: {yt.author}')


@bot.message_handler()
def youtubedownload(message):
    text = message.json['text']
    if text.startswith == 'https://www.youtube.com/' or  text.startswith == "https://www.youtu.be/":
        yt = YouTube(text)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        stream.get_highest_resolution().download(f'{message.chat.id}', f"{message.chat.id}_{yt.title}")
        with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
            bot.send_video(message.chat.id, video, caption='*вot ваше видео*', parse_mode='Markdown')
            os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')
        



bot.polling(none_stop=True)
 