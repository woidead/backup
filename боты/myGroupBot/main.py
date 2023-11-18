import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import token
API_TOKEN = token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот для модерации группы. "
                        "Чтобы забанить пользователя, используйте /ban. "
                        "Чтобы дать мут, используйте /mute время_в_секундах."
                        "Все команды должны быть ответом на сообщения наказуемого")


@dp.message_handler(commands=['ban'])
async def ban_user_by_reply(message: types.Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_to_ban = message.reply_to_message.from_user
        await message.chat.kick(user_to_ban.id)
        await message.reply(f"Пользователь {user_to_ban.mention} забанен.")


@dp.message_handler(commands=['mute'])
async def mute_user_by_reply(message: types.Message):
    if  message.reply_to_message and message.reply_to_message.from_user:
        user_to_mute = message.reply_to_message.from_user
        mute_time = int(message.text.split()[-1])
        
        await message.chat.restrict(user_to_mute.id, permissions=types.ChatPermissions())
        await message.reply(f"Пользователь {user_to_mute.mention} получил мут на {mute_time} секунд.")
        await asyncio.sleep(mute_time)
        await message.chat.restrict(user_to_mute.id, permissions=types.ChatPermissions(can_send_messages=True))
        await message.reply(f"Пользователь {user_to_mute.mention} вышел из мута длинной на {mute_time} секунд.")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
