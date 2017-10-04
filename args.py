import os, sys

def test_var_args(f_arg, *argv):
    print("first normal arg:" , f_arg)
    for arg in argv:
        print("another arg through *argv", arg)
test_var_args('salim', 'python', 'cats', 'test')



def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key,value))
greet_me(name="Salim")



def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)
args = ("two", 3, 5)
test_args_kwargs(*args)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)


# So if you want to use all three of these in functions then the order is some_func(fargs, *args, **kwargs)
