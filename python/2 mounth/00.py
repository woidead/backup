data = open(r'hello.txt', 'a', encoding='utf-8')
file = data.write('hello aziz')
print(file)
data.close()
