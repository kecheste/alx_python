def common_elements(set_1, set_2):
    comm = []
    for x in set_1:
        if x in set_2:
            comm.append(x)
    return comm
