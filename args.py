#if you want to use all three types of arguments in functions then the order is func(fargs, *args, **kwargs)
#The most common use case is when making function decorators or modifying  code at runtime.
# Using fargs, *args and **kwargs

def test_var_args(fargs, *argv):
    print("first normal arg:" , fargs)
    for arg in argv:
        print("another arg through *argv", arg)
test_var_args('Salim', 'python', 'cats', 'test')



def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key,value))
greet_me(name="Salim")



def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)
args = ("two", 3, 5)                                # tuple
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}      # dictionary
largs = [{"two":456},  (4,5), {'abc':123}]          # list
print "*args using tuple"
test_args_kwargs(*args)
print "*largs using list"
test_args_kwargs(*largs)
print "**kwargs using dictionary"
test_args_kwargs(**kwargs)





