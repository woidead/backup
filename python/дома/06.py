
# Создайте класс ПЕРСОНА с методами, позволяющими вывести на экран информацию о персоне, а также определить ее возраст
#  (в текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет), СТУДЕНТ (фамилия, дата
#  рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж), со своими методами
#  вывода информации на экран и определения возраста
# В родительском классе Persona() определим, в соответствии с условием задачи, метод vozrast(), служащий для определения
#  возраста и метод info(), позволяющий вывести информацию о персоне. Далее создаем три дочерних класса: Abiturient
# (Persona), Student(Persona), Prepodavatel(Persona), основанные на классе Persona(). Соответственно, все дочерние 
# классы будут наследовать методы родительского класса.
class Persone:
    def __init__(self, name, yob):
        
        self.name = name
        self.yob = yob
    def infop(self):
        s = 2022 - {self.yob}
        print(f'{self.name} {s} y.o. {self.yob} year of birth')

class Applicant(Persone):
    def __init__(self, surname, yobd, faultet):
        self.surname = surname
        self.yobd = yobd
        self.faultet = faultet
    #def infoa(self):
        #print(f'{self.surname} {yobd} {self.faultet} ')

#aa = Applicant('umarov', 2005, 'python')

#aa.infoa()