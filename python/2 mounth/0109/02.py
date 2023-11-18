#getter, setter
class Counter:
    c= 0
    def setter(self, count ):
        self.count = count 
        self.c += self.count 

    def getter(self):
        return self.c
    
co = Counter() 
co.setter(45) #вставка
co.getter()   #вывод
co.setter(45)
co.setter(45)

print(co.getter())

