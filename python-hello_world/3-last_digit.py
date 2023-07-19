import random
number = random.randint(-10000, 10000)
numberstr = str(number)
word = " "
if int(numberstr[-1]) > 5:
    word = "and is greater than 5"
elif int(numberstr[-1]) == 0:
    word = "and is 0"
elif int(numberstr[-1]) < 6 and not 0:
    word = "and is less than 5 and not 0"
print("Last digit of {} is {} {}".format(numberstr, numberstr[-1], word))