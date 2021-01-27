##python decorators


def print_lowercase(data):
    return data.lower()

#print(print_lowercase('Shubham'))

def uppercase_decorator(func):
    def wrapper():
        data = func()
        return data.upper()
    return wrapper

def say_hi():
    return 'hello_there'

decorator = uppercase_decorator(say_hi)
print(decorator())

####
print("from different way...calling decorator............")


@uppercase_decorator
def say_hello():
    return 'hello_there'

print(say_hello())


#########################

print("decorators accepting arguments...........")


def decorator_with_arguments(func):
    def wrapper_to_accept_arguments(arg1, arg2):
        print("these are arguments to function {},{}".format(arg1, arg2))
        return func(arg1, arg2)

    return wrapper_to_accept_arguments

@decorator_with_arguments
def display_names(name1, name2):
    print("names are {}, {}".format(name1, name2))

display_names('shubham', 'sharma')


####################################3

print('GENERAL PURPOSE DECORATORS.......')

def general_decorator(function):
    def general_wrapper(*args, **kwargs):
        print('positional args are ', args)
        print('keyword args are ', kwargs)

        return function(*args, **kwargs)

    return general_wrapper

@general_decorator
def function_with_no_args():
    print('no args passed..')

function_with_no_args()

@general_decorator
def function_with_args(a,b):
    print('passed args are {} , {}'.format(a,b))



function_with_args('delhi','bombay')



