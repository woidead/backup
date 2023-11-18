import random
import string

def generate_password(length: int, special: bool = True, numbers: bool = True):
    alphabet = string.ascii_letters 
    if special:
        alphabet += string.punctuation
    if numbers:
        alphabet += string.digits
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

while True:
    iq = int(input('длина: '     ))
    f = bool(input('Знаки: '))
    x = bool(input('Цифры: '))
    password = generate_password(iq, special=f, numbers=x)
    print(password)
    