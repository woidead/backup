# 1) Создать класс Phone, у него должен быть атрибут , изначальное значение которого равно 100% и 
# метод turnOn(), который при вызове понижает процент заряда телефона на 10%, также должен быть метод charge(), 
# при вызове которого заряд повышается на 10%, но главное, нельзя чтобы он заряжал его больше чем на 100%.
class Phone:
    battery = 100
    def turon(self):
        if self.battery>0:
            self.battery -= 10
            print(self.battery)
    def charge(self):
        if self.battery<100:
            self.battery += 10
            print(self.battery)
    def static(self):
        print(self.battery)

iphone = Phone()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.turon()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.charge()
iphone.static()


