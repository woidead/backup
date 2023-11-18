import os
from PIL import Image
from moviepy.editor import *
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher.filters import Photo
# from aiogram.dispatcher.filters import Video
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = '6062796417:AAEPkwspM8CyGY63X6GEdf2cbHJIsp4_hBM'  # Вставьте токен вашего телеграм-бота
MAX_SIZE = 256  # Максимальный размер файла (в кб) для сжатия

bot = Bot(token=TOKEN)

# Инициализация хранилища состояний
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Функция для изменения формата и сжатия изображений
async def convert_image(image_path, output_path, max_size=256):
    with Image.open(image_path) as img:
        # Пропорционально изменяем размер изображения, если его размер превышает максимально допустимый
        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
        img.save(output_path)


# Функция для изменения формата и сжатия видео
async def convert_video(video_path, output_path, max_size=256):
    video = VideoFileClip(video_path)
    # Пропорционально изменяем размер видео, если его размер превышает максимально допустимый
    if video.size[0] > max_size or video.size[1] > max_size:
        video = video.resize(height=max_size)
    video.write_videofile(output_path, codec='libvpx')


# Обработчик команды /start
@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    """
    Команда /start

    Отправляет приветственное сообщение с описанием функций бота.
    """
    await message.reply("Привет! Я бот для конвертации формата фото и видео в webm и сжатия до 256 кб.\n"
                        "Отправь мне фото или видео и я сделаю все остальное!")


# Обработчик фото
@dp.message_handler(content_types=['photo'])
async def process_photo(message: types.Message, state: FSMContext):
    """
    Обработчик фото

    Изменяет формат фото на webm и сжимает до 256 кб.
    """
    await message.reply("Обработка фото...")

    # Скачиваем фото во временную папку
    photo = await bot.download_file(message.photo[-1], timeout=60)

    # Создаем папку для сохранения конвертированных файлов
    if not os.path.exists('converted'):
        os.makedirs('converted')
        # Определяем пути для сохранения оригинального и конвертированного файла
    original_file = f'{message.from_user.id}_original.jpg'
    converted_file = f'{message.from_user.id}_converted.webm'

    # Конвертируем фото
    await convert_image(photo, original_file, max_size=MAX_SIZE)
    await convert_video(original_file, converted_file, max_size=MAX_SIZE)

    # Отправляем конвертированный файл пользователю
    with open(converted_file, 'rb') as f:
        await bot.send_document(message.chat.id, f, caption='Конвертированное фото в формате webm')

    # Удаляем временные файлы
    os.remove(photo)
    os.remove(original_file)
    os.remove(converted_file)

    # Завершаем состояние
    await state.finish()
@dp.message_handler(content_types=['video'])
async def process_video(message: types.Message, state: FSMContext):

    await message.reply("Обработка видео...")

    # Скачиваем видео во временную папку
    video = await bot.download(message.video, timeout=60)

    # Создаем папку для сохранения конвертированных файлов
    if not os.path.exists('converted'):
        os.makedirs('converted')

    # Определяем пути для сохранения оригинального и конвертированного файла
    original_file = f'{message.from_user.id}_original.mp4'
    converted_file = f'{message.from_user.id}_converted.webm'

    # Конвертируем видео
    await convert_video(video, original_file, max_size=MAX_SIZE)
    await convert_video(original_file, converted_file, max_size=MAX_SIZE)

    # Отправляем конвертированный файл пользователю
    with open(converted_file, 'rb') as f:
        await bot.send_document(message.chat.id, f, caption='Конвертированное видео в формате webm')

    # Удаляем временные файлы
    os.remove(video)
    os.remove(original_file)
    os.remove(converted_file)

    # Завершаем состояние
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
