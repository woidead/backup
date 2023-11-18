def is_four_digit(num):
    return abs(num) >= 1000 and abs(num) <= 9999

def main():
    count_pairs = 0
    max_sum = 0

    with open("17_9840.txt", "r") as file:
        sequence = list(map(int, file.read().split()))
    for i in range(len(sequence) - 1):
        num1, num2 = sequence[i], sequence[i + 1]
        if (is_four_digit(num1) and not is_four_digit(num2)) or (not is_four_digit(num1) and is_four_digit(num2)):
            if (num1 + num2) ** 2 < 9239 ** 2:
                count_pairs += 1
                max_sum = max(max_sum, num1 + num2)

    print(f"{count_pairs} {max_sum}\n")


    max_number = float("-inf")

    for num in sequence:
            if 1000 <= num <= 9999 and num % 100 == 39:
                max_number = max(max_number, num)


if __name__ == "__main__":
    main()
