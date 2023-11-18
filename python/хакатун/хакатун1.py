class Soda:
    def __init__(self, Add = 'обычный'):
        self.Add = Add
    def show_my_drink(self):
        if self.Add == 'добавка':
            print('газировка и добавка')
        elif self.Add == 'обычный':
            print('обычная газировка')

#s = Soda('добавка')
s = Soda()
s.show_my_drink()