# import random
# while True:
#     lst = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     m =  int(input('kol: '))
#     lst1 = ["#"+''.join([random.choice(lst) for j in range(6)])for i in range(m)]
#     print(lst1)
# class Luck:
#     def __init__(self, c = 1) :
#         self.c = c
#     def lucky(self, c):
#         b = 0
#         a = 0
#         for x in range(0,3):
#                 b = b + int(str(c)[x])
#         for d in range(3,6):
#                 a = a + int(str(c)[d])
#         if a == b:
#             print('вы выиграли счастливый билет')
#         else:
#             print('к сожалению вы проиграли')
#         print('номер вашего билета:', c)

# luck = Luck()
# luck.lucky(123453)







# d = (random.choices(lst, k=6))
# d[0:6] = [''.join(d[0:6])]
# d =(', '.join(d))
# lst1.append(d)
# # lst1=(', '.join(lst1))
# lst1[0:2] = [''.join(lst1[0:2])]


# class User():
#     def __init__(self, name, email):
#         self.name = name 
#         self.email = email
#     def get_init(self):
#         print(f'{self.name}-{self.email}')
#     @classmethod
#     def get_into_class(cls, ls = [1,2]):
#         a, b =ls
#         print(f'{a}-{b}')
# lst = ['erlan', 'erlan@gmail.com']
# user = User
# user.get_into_class(lst)



