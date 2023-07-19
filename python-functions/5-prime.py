def is_prime(number):
    flag = True
    for i in range(2, number):
        if (number % i) == 0:
            flag = False
            break
    return flag