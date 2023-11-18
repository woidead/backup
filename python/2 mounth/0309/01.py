#инкапсуляция это упаковка данных и функций, рабоатающих с этими данными, в один компонент и ограничение доступа к некоторым 
#компонентам объекта
#инкапсуляция скрытие информации
#Создать банкомат класс называется ATM. У класса есть конструкторю который принимает атрибуты name, _id, __password
#И нужно создать метод  public_method(), который нам показывает Имя пользователя.
#И еще создать защищенный метод protectedMethod(), который нам показывает Имя пользователя с id
#И есть приватный метод privateMethod(), который нам показывает Имя пользователя, id и пароль
class ATM:
    def __init__(self, name, id, password):
        self._id = id
        self.name = name
        self.__password = password
    def _protectedMethod(self):
        print(f'{self._id} {self.name}')
    def __privateMethod(self):
        print(f'{self._id} {self.__password}')
con = ATM('amir','#001122', '22000111')
con._protectedMethod()
con._ATM__privateMethod()
con.__password = 222