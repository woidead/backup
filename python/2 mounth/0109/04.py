class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        print((self.name),'is', (self.age), 'years')
    def speak(self, sound):
        
        print((self.name), 'says', (sound))
dog = Dog('jack', 3,)
dog.description()
dog.speak('woof woof')