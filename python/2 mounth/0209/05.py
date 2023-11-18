class Person:
    def __init__(self, name, surname, gender="m"):
        self.name = name
        self.surname = surname
        self.gender = gender
    def tt(self):
        if self.gender == "m":
            print(f'Гражданин {self.surname} {self.name}')
        elif self.gender == 'f':
            print(f'Гражданка {self.surname} {self.name}')
        else:
            print(f'Не знаю, что вы имели ввиду? Пусть это будет мальчик! Гражданин {self.surname} {self.name}')


person = Person('Асанова','Севара', 'f')
person.tt()

