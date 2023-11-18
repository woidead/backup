def plusOne(digits):
    char = ''
    lst = []

    for i in digits:
        char += str(i)

    char = str(int(char) + 1)

    for i in char:
        lst.append(int(i))

    print(lst)

plusOne([9])