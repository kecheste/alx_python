def no_c(my_string):
    for c in my_string:
        if c == 'c' or c == 'C':
            c = ''
        print(c, end="")

no_c('Holberton School')