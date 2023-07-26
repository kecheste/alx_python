def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{}".format(col), end=" " if col != row[-1] else "")
        print('$')

    # OR

    # for e in matrix:
    #     for i in e:
    #         print('{:d}'.format(i), end='')
    #         if i != e[-1]:
    #             print(' ', end='')
    #     print("")
