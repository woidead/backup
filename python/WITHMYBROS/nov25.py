import time
# """-----Наследование и полиморфизм-----"""

# ">>> Наследование <<<"

# class Shape():

#     def __init__(self):
#         print('Shape created')

#     def draw(self):
#         print('Drawing a shape')

#     def area(self):
#         return 'Calc area'


#     def perimetr(self):
#         print('Calc perimetr')

# # shape = Shape()


# class Rectangle(Shape):   # Дочерный класс или же наследник

#     def __init__(self, width, heigth):

#         Shape.__init__(self)

#         self.width = width
#         self.heigth = heigth

#         print('Rectangle created')

#     def draw(self):
#         print('Drawing a rectangle')

#     def area(self):  # Переопределение  метода базового класса
#         return self.width * self.heigth
    
#     def perimetr(self):   # Переопределение  метода базового класса
#         return 2 * (self.width + self.heigth)

# rect = Rectangle(4,5)
# rect.draw()

# class Triangle(Shape):   # Дочерный класс или же наследник

#     def __init__(self, a, b, c):
#         # Shape.__init__(self)
#         self.a = a
#         self.b = b
#         self.c = c
        
#     # def area(self):  # Переопределение  метода базового класса
#     #     return self.a * self.a
    
#     def perimetr(self):   # Переопределение  метода базового класса
#         return (self.a + self.b + self.c)

# tri = Triangle(5,5,5)
# print(tri.perimetr())



# # ">>> Полиморфизм <<<"

# for shape in [rect, tri]:
#     print(shape.area())
# # множественное наследоание
# class Cls(Triangle, Rectangle):
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth =heigth
# cls = Cls(4, 7)
# print(cls.area())

# class Vehicle():
#     def __init__(self, year, color, clas, category ):
#         self.year = year
#         self.color = color
#         self.clas = clas
#         self.categoty = category
# class Car(Vehicle):
#     def __init__(self, year, color, clas, category, model):
#         super().__init__(year, color, clas, category)
#         self.model = model
# a = input('year: ')
# b = input('color: ')
# c = input("class: ")
# d = input("category: ")
# e = input("model: ")
# car = Car(a, b, c, d, e)
# print(car.__dict__)
class FlourProducts():
    def __init__(self, wheat, flour, eggs, oil, salt, water):
        self.wheat = wheat
        self.flour = flour 
        self.eggs = eggs
        self.oil = oil
        self.salt = salt
        self.water = water
class Cake(FlourProducts):
    def __init__(self, wheat, flour, eggs, oil, salt, water, sugar, cacao):
        super().__init__(wheat, flour, eggs, oil, salt, water)
        self.sugar = sugar
        self.cacao = cacao
class Samsa(FlourProducts):
    def __init__(self, wheat, flour, eggs, oil, salt, water, meat):
        super().__init__(wheat, flour, eggs, oil, salt, water)
        self.meat = meat
    def cook(self):
        print('тесто готово')
    def fry(self):
        print('тесто в духовке')
        time.sleep(2.5)
        print('вытаскивай из духовки')
test = Samsa('пшеничная', 'мука', 'яйца', 'подсолнечное масло', ' соль', 'из под крана', 'бычье')
print(test.__dict__)
test.cook()
test.fry()
