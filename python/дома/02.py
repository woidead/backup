# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод init(), внутри которого будут определены два динамических свойства: 1) lang - язык и 
# 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите

a1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a3 = "abcdefghijklmnopqrstuvwxyz"
a4 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        len(self.letters)
alphabet = Alphabet('eng', a2)
alphabet.print()
alphabet.letters_num()
