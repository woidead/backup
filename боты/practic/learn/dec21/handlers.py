from dec21.main import bot, dp
from aiogram.types import Message
from dec21.config import admin_id
async def send_to_admin1(dp):
    await bot.send_message(chat_id = admin_id, text = 'bot started')
async def send_to_admin2(dp):
    await bot.send_message(chat_id = admin_id, text = 'bot finished')
@dp.message_handler()
async def echo(message: Message):
    text = f'@{message.from_user.username}({message.from_user.id}) texted: "{message.text}"'
    await bot.send_message(chat_id = admin_id, text = text)
    # await message.answer(text = text)