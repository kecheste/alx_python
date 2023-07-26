def update_dictionary(a_dictionary, key, value):
    dict(a_dictionary)
    a_dictionary |= {key : value}
    for el in a_dictionary:
        print("{}: {}".format(el,a_dictionary.get(el)))
