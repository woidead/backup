def is_not_four(num):
    return abs(num) < 1000 

def main():
    with open('17_9786.txt', 'r') as file:
        sequense= list(map(int, file.read().split()))
        max_number=0
        counter =0
        max_sum = 0
        for num in sequense:
            if num > max_number and num%100==25:
                max_number = num
        try:
            for i in range(len(sequense)-3):
                num1, num2, num3 = sequense[i], sequense[i+1], sequense[i+2]
                if is_not_four(num1) or is_not_four(num2) or is_not_four(num3):
                    if (num1+ num2+ num3) < max_number:
                        counter+=1
                        max_sum=(max((num1+ num2+ num3), max_sum))
        except:
            print(2)
        print(counter, max_sum)
main()