#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number - (10 * int(number / 10))
word = " "
if last_digit > 5:
    word = "and is greater than 5"
elif last_digit == 0:
    word = "and is 0"
elif last_digit < 6 and not 0:
    word = "and is less than 5 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, word))