from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(TOKEN)
dp = Dispatcher(bot)
HELP_TEXT='''
/help - все команды
/start - начало
/sticker
/photo
/video
все вопросы к @woidead
'''
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/sticker')
b3 = KeyboardButton('/photo')
b4 = KeyboardButton('/start')
kb.add(b1).insert(b2).insert(b3).add(b4)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id, 
        text='добро поjаловать',
        reply_markup=kb
    )

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
        await bot.send_message( 
                        message.from_user.id, 
                        text=HELP_TEXT, 
                        reply_markup=ReplyKeyboardRemove()
                        )



async def start_up(_):
    print('bot started')
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_up)