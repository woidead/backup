# from faker import Faker
# m = Faker('ru_RU')


# people = []
# for i in range(10):
#     people.append(m.name())
# print(people)

# z = [job for job in m.name()]
# print(z)

# x = [i for i in range(1, 100)]
# print(x)


# students = [ 
#     {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'}, 
#     {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'}, 
#     {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'}, ]


# x = [i.get('course', '') for i in students] #если в массиве нет значения course, то будет добавлять пустую строчку


# (values) = [(expression) for (value) in (collection)] #формула генераторов списков



# ФИЛЬТРАЦИЯ

# x  = [i['name'] for i in students if i['age'] >= 30]

# students = ['Ravshan', 'Akhror', 'Rayana', 'Ajymkan', 'Nurislam']

# for i in students:
#     if i[0] == 'R':
#         print(i)

# x = [i for i in students if i[0] == 'R']
# print(x)


# names = ['jonh', 'michel', 'leon', 'denis']

# x = [i for i in names if i.startswith('j')] #фильтрация по началу имени


# (values) = [(expression) for (value) in (collection) if (condition)] #формула фильтрации генераторов списков









print(x)    