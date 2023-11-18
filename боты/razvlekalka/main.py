import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import token
import sqlite3
import datetime

API_TOKEN = token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Подключение к базе данных (SQLite)
conn = sqlite3.connect('trees.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        tree_height INTEGER,
        last_change TIMESTAMP
    )
''')
conn.commit()

# Функция для получения текущей высоты дерева пользователя
def get_tree_height(user_id):
    cursor.execute('SELECT tree_height FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return 0

# Функция для изменения высоты дерева пользователя
def change_tree_height(user_id, amount):
    current_height = get_tree_height(user_id)
    new_height = max(min(current_height + amount, 200), 0)
    cursor.execute('INSERT OR REPLACE INTO users (user_id, tree_height) VALUES (?, ?)', (user_id, new_height))
    conn.commit()
    return new_height

# Функция для случайного изменения высоты дерева
async def random_change_tree_height(user_id):
    change_amount = random.randint(-15, 10)  # Случайное изменение от -10 до 10 см
    new_height = change_tree_height(user_id, change_amount)
    return new_height, change_amount

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply(f'я бот который может развлечь тебя \nнапиши "/dick" \n или "/current_size"')

@dp.message_handler(commands=['current_size'])
async def current_size(message:types.Message):
    current_height = get_tree_height(message.from_user.id)
    await message.reply(f'твой хуй на данный момент {current_height} см')


# Обработчик команды /tree
@dp.message_handler(commands=['dick'])
async def tree_command(message: types.Message):
    user_id = message.from_user.id
    # Проверяем, прошел ли уже день с момента последнего изменения дерева
    cursor.execute('SELECT last_change FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result and result[0]:
        last_change = datetime.datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S.%f')
        now = datetime.datetime.now()
        time_difference = now - last_change
        if time_difference.days < 1:
            await message.reply("Твой хуй уже сегодня достаточно вырос. Попробуй завтра.")
            return
    
    new_height = await random_change_tree_height(user_id)
    
    await message.reply(f"Вы изменили высоту дерева на {new_height} см.")

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)




