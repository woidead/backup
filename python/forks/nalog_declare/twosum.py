# генерация паролей на пайтон_
import random, string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
znaki = string.ascii_letters + string.digits + string.punctuation
password=''
for i in range(8):
    password +=(random.choice(znaki))

print(password)
