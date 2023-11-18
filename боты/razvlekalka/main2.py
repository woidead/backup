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

# Функция для преобразования высоты в формат метры и сантиметры
def format_height(height):
    if height >= 200:
        meters = height // 100
        centimeters = height % 100
        return f"{meters} м {centimeters} см"
    else:
        return f"{height} см"

# Функция для случайного изменения высоты дерева
async def random_change_tree_height(user_id):
    change_amount = random.randint(-10, 10)  # Случайное изменение от -10 до 10 см
    current_height = get_tree_height(user_id)
    new_height = current_height+change_amount
    cursor.execute('INSERT OR REPLACE INTO users (user_id, tree_height, last_change) VALUES (?, ?, ?)', (user_id, new_height, datetime.datetime.now()))
    conn.commit()
    return new_height, change_amount

# Обработчик команды /tree
@dp.message_handler(commands=['tree'])
async def tree_command(message: types.Message):
    user_id = message.from_user.id
    
    # Проверяем, прошло ли уже 5 минут с момента последнего изменения дерева
    cursor.execute('SELECT last_change FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result and result[0]:
        last_change = datetime.datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S.%f')
        now = datetime.datetime.now()
        time_difference = now - last_change
        if time_difference.seconds < 1:
            await message.reply("Вы уже меняли высоту дерева недавно. Попробуйте позже.")
            return
    
    new_height, change_amount = await random_change_tree_height(user_id)
    
    formatted_height = format_height(new_height)
    await message.reply(f"Вы изменили высоту дерева на {formatted_height}. Изменение: {change_amount} см")

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
