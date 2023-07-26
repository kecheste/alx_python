def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    except:
        result = None
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))