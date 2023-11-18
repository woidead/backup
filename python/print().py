from random import choice
prefix = '+0444'
num = '145790'
length = 6
def gen_number():
    result =''
    for _ in range(length):
        result += choice(num) 
    return prefix + result

print(gen_number())