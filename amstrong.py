def is_armstrong(number):
    num = str(number)
    p = len(num)
    sum_of_digits = sum(int(digit) ** p for digit in num)
    return sum_of_digits == number
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")