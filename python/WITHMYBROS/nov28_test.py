import unittest
class Luck(unittest.TestCase):
    def test_lucky(self, c):
        
        a, b = 0, 0
        for x in range(0,3):
                b = b + int(str(c)[x])
        for d in range(3,6):
                a = a + int(str(c)[d])
        if a == b:
            print('вы выиграли счастливый билет')
        else:
            print('к сожалению вы проиграли')
        print('номер вашего билета:', c)
luck = Luck()
luck.test_lucky(2)
# a = 10_000
# b = 20000
# c = a * b
# print(f'{c:,}')
