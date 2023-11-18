################################################
# Создать класс Salary. У него должно сеттер и геттер методы. Сеттер принимает 2 аргументa name, salary.
#  В геттер должен вывести "<name> зарабатывает в месяц <salary>"
# Создать метод сountofYear, который посчитает сколько зарабатывает в год
#  <name> зарабатывает в год <salary>" 
class Salary:
    def set(self, name, salary):
        self.name = name
        self.salary = salary
    def get(self):
        print(f'{self.name} зарабатывает в месяц {self.salary} долларов')
    def year(self):
        s = (self.salary) * 12
        print(f'за год у {self.name} выходит {s} долларов')

john = Salary()
john.set('John', 1200 )
john.get()
john.year()