#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'Last digit of {number} is {str(number)[-1]} and is ', end='')
if int(str(number)[-1]) > 5:
    print("greater than 5")
elif int(str(number)[-1]) == 0:
    print("is 0")
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
    print("less than 6 and not 0")
