# #constants
# class Aziz():
#     MAXSPEED = 100
#     def __init__(self, race, damage=1):
#         self.race=race
#         self.damage=damage
# c = Aziz('elf')
# c.MAXSPEED = 900
# print(c.MAXSPEED)



# защищенные  и приватные
# class Aziz():
#     MAX_SPEED=100 #constant
#     def __init__(self, race, damage =1):
#         self.damage = damage
#         self._health = 50
#         self.__race = race
#     @property
#     def hit(self, damage):
#         self._health -= damage
#     @property
#     def race(self):
#         return self.__race
#     @property # возможность работбать с защищ знач вне класса
#     def current_speed(self):
#         return self._current_speed
#     @current_speed.setter # 
#     def current_speed(self, current_speed):
#         self._current_speed = current_speed





# c = Aziz('elf')
# c.current_speed = 10
# print(c.current_speed) #print(c._Aziz__race) вывести защищенный

        

