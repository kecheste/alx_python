def fibonacci_sequence(n):
    if n <= 0:
        return []
    
    fibonacci_numbers = []
    a, b = 0, 1

    for i in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b
        
    return fibonacci_numbers