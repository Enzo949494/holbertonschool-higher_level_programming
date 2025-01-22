#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    output = ""
    try:
        for i in range(x):
            output += str(my_list[i])
            printed += 1
    except:
        pass
    finally:
        print(output)
    return printed
