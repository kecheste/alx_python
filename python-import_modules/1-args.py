import sys

arguments = sys.argv
arguments.pop(0)

if(len(arguments) == 0):
    print('0 arguments.')
elif(len(arguments) == 1):
    print('1 argument:')
    print("1: {}".format(arguments[0]))
else:
    print('{} arguments:'.format(len(arguments)))
    j = 0
    for i in arguments:
        j += 1
        print("{}: {}".format(j,i))