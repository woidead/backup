from PIL import Image
from moviepy.editor import *
import os

# Функция для изменения формата и сжатия изображений
def convert_image(image_path, output_path, max_size=256):
    with Image.open(image_path) as img:
        # Пропорционально изменяем размер изображения, если его размер превышает максимально допустимый
        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
        img.save(output_path)

# Функция для изменения формата и сжатия видео
def convert_video(video_path, output_path, max_size=256):
    video = VideoFileClip(video_path)
    # Пропорционально изменяем размер видео, если его размер превышает максимально допустимый
    if video.size[0] > max_size or video.size[1] > max_size:
        video = video.resize(height=max_size)
    video.write_videofile(output_path, codec='libvpx')

# Основной код
input_path = "example.png"  # Путь к входному файлу (изображению или видео)
output_path = "example.webm"  # Путь к выходному файлу (webm)

if input_path.endswith(".png"):
    # Если входной файл - изображение в формате jpg
    convert_image(input_path, output_path)
elif input_path.endswith(".mp4"):
    # Если входной файл - видео в формате mp4
    convert_video(input_path, output_path)
else:
    print("Неподдерживаемый формат файла")

# Проверяем размер выходного файла, и если он больше 256 кб, сжимаем его до 256 кб
if os.path.getsize(output_path) > 256 * 1024:
    if output_path.endswith(".jpg.webm"):
        # Если выходной файл - изображение, перезаписываем его сжимая до 256 кб
        convert_image(output_path, output_path, max_size=256)
    elif output_path.endswith(".mp4.webm"):
        # Если выходной файл - видео, перезаписываем его сжимая до 256 кб
        convert_video(output_path, output_path, max_size=256)
else:
    print("Выходной файл уже имеет размер не более 256 кб")
