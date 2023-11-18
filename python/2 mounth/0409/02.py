class Human:
    def __init__(self, name, age, gender):
        self.name= name
        self.age = age
        self.gender = gender
    def get(self):
        print(f'{self.name}, is {self.age} years old. he is {self.gender}')
class Worker:
    def __init__(self, wname, wage, wgender, profession,):
        self.profession = profession
        self.infow = Human(name=wname, age=wage, gender=wgender)
    def show(self):
        print(f'my name {self.infow.name}. im {self.infow.age}. im {self.infow.gender}. my profession {self.profession}')
he = Worker('jo', 19, 'male', 'streamer')
he.show()






    