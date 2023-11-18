# в  ооп есть 4 концепций
# абстракцияб композиция
#наследование
#полиморфизм
#инкапсуляция
#наследование - это возможность
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
print(cat.age)
class Tiger(Cat):
    pass
tiger = Tiger('sher', 3)
print(tiger.age)
print(tiger.info)

