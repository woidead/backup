from turtle import color
from unicodedata import name


class Cat:
    paws = 4
    tail = 1 
    ears = 2
    def __init__(self, name, color, age) :
        self.name = name
        self.color = color
        self.age = age

    def info(self):
        print(self.paws)
cat = Cat('мурзик', 'черный', 7)
cat.info()
print(cat.age) #чтобы вывести надо print(переменнная с информацией.что мы хочем вывести)
#геттер, сеттер