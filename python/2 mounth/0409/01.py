


class Address:
    def __init__(self, city, district, street, home):
        self.city = city
        self.district = district
        self.street = street 
        self.home = home
class Profession:
    def __init__(self, prof, jobaddress, salary):
        self.prof = prof
        self.jobaddress = jobaddress
        self.salary = salary
class Worker:
    def __init__(self, name, w_city, w_district, w_street, w_home, w_prof, w_jobaddress, w_salary):
        self.name = name
        
        self.address= Address(city=w_city, district=w_district,street=w_street, home=w_home)
        self.proffesion=Profession(prof=w_prof, jobaddress=w_jobaddress, salary=w_salary)

    def printDate(self):
        print(f'{self.name}')
        print(f'City : {self.address.city}')
    def info(self):
        print(f'{self.name}, {self.address.district} {self.address.city} {self.address.home} {self.address.street}  {self.proffesion.jobaddress} {self.proffesion.salary} {self.proffesion.prof} ')

he = Worker('jo', 'london', 'manas', 'manas', 22, 'developer', 'google', 1000000 )
he.printDate()
he.info()