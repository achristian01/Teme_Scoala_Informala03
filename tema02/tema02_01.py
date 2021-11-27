# Update of the code, Aug 29

def ssum(*args):

    sum_args = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum_args += i

    return print("The sum of numeric arguments in our list is: ", sum_args)


print(ssum("q", "a", 5, 5, 3.0))

