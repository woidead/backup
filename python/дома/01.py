# Задание 2
# Напишите программу с классом Car. Создайте конструктор класса Car. 
# Создайте __init__ атрибуты класса Car — color (цвет), type (тип), year (год). 
# Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. 
# Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.:

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        print('машина заведена')
    def stop(self):
        print('автомобиль заглушен')
    def info(self):
        print('color', self.color)
        print('type', self.type)
        print('year', self.year)
car = Car('black', 'supra', '1991')
car.info()   
car.stop()
car.start()