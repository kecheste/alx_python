def no_c(my_string):
#     new_string = my_string.translate({ord(i): None for i in 'cC'})
#     return new_string
#     OR
    new_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str