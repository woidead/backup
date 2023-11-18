import logging
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import token
API_TOKEN = token
import pip
pip.main(['install', 'aiogram'])
logging.basicConfig(level=logging.INFO)
from background import keep_alive
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот для модерации группы. "
                        "Чтобы забанить пользователя, используйте /ban. "
                        "Чтобы дать мут, используйте /mute время_в_секундах."
                        "Все команды должны быть ответом на сообщения наказуемого")

async def is_admin(message: types.Message) -> bool:
    chat_member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return chat_member.status in ("administrator", "creator")


@dp.message_handler(commands=['ban'])
async def ban_user_by_reply(message: types.Message):
    if message.reply_to_message and message.reply_to_message.from_user and await is_admin(message):
        user_to_ban = message.reply_to_message.from_user
        await message.chat.kick(user_to_ban.id)
        await message.reply(f"Пользователь {user_to_ban.mention} забанен.")
    else:
        await message.reply('gandon ты не админ')


@dp.message_handler(commands=['mute'])
async def mute_user_by_reply(message: types.Message):
    if message.reply_to_message and message.reply_to_message.from_user and await is_admin(message):
        user_to_mute = message.reply_to_message.from_user
        mute_time = int(message.text.split()[-1])
        
        await message.chat.restrict(user_to_mute.id, permissions=types.ChatPermissions())
        await message.reply(f"Пользователь {user_to_mute.mention} получил мут на {mute_time} секунд.")
        await asyncio.sleep(mute_time)
        await message.chat.restrict(user_to_mute.id, permissions=types.ChatPermissions(can_send_messages=True))
        await message.reply(f"Пользователь {user_to_mute.mention} вышел из мута длиной на {mute_time} секунд.")
    else:
        await message.reply('у меня других дел нет? не работаю на обычных смертных')

keep_alive()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
