def fibonacci_sequence(n):
    n1, n2 = 0, 1
    i = 0

    if n <= 0:
        return "Enter positive integer"
    elif n == 1:
        return n1
    else:
        while i < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            i += 1