import asyncio
from aiogram import Bot, Dispatcher, executor
from dec21.config import TOKEN


loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop = loop)

if __name__=='__main__':
    from dec21.handlers import dp, send_to_admin1, send_to_admin2
    executor.start_polling(dp, on_startup=send_to_admin1)
    executor.start_polling(dp, on_shutdown=send_to_admin2)
    




