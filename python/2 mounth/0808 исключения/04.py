a = int(input('1: '))
b = int(input('2: '))
try:
    print(a)
    print(b)
    print('a/b=',a/b)
except ZeroDivisionError:
    print('ТЫ ДЕБИЛ')
else:
    print(a/b)
finally:
    print('я удивлен твоей логикой')