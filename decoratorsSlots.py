# def hi(name='Salim'):
#     return "hi " + name
# print hi()
#
# greet = hi     # assign a function to a variable
#
# print greet()
#
# del hi
# #print hi()
# print greet()

import os, requests

def hi(name='Salim'):
    print "Inside hi function"

    def greet():
        return "Inside greet function"

    def welcome():
        return "Inside welcome function"


    if name == 'Salim':
        return greet
    else:
        return welcome

    #print greet()
    #print welcome()
    #print "Now back in the hi function"

# git commit 3, 4, 5

a = hi()
print "a = " , a
print "a() = ", a()

a = hi('World')
print "a = " , a
print "a() = ", a()


def hello():
    return "hi Salim"

def doInit(func):
    print "Initial work before hello()"
    print func()

doInit(hello)


from functools import wraps

def a_new_decorator(func):
    @wraps(func)
    def wrapTheFunction():
        print "Before executing func()"
        func()
        print "After executing func()"
        return func()
    return wrapTheFunction

@a_new_decorator
def b_func():
    ''' This function is passed into decorators'''
    print "This function needs decorators"


#b_func = a_new_decorator(b_func)
b_func()
print b_func.__name__

print "============="


from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return "Function is running"

can_run = True
print func()

can_run = False
print func()


from functools import wraps

def logit(logfile='/tmp/out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print log_string
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
                opened_file.close()
        return wrapped_function
    return logging_decorator


@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='/tmp/func2.log')
def myfunc2():
    pass

myfunc2()



class logit(object):
    def __init__(self, logfile = '/tmp/outclass.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + " was called"
        print log_string

        with open(self.logfile, 'a') as opened_file :
            opened_file.write(log_string + '\n')
        self.notify()

    def notify(self):
        pass


@logit()
def myfunction1():
    pass



class email_logit(logit):
    def __init__(self, email = 'abc@project.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        pass


print "\n\n Using __slots__ to save memory for class instances"

#import ipython_memory_usage.ipython_memory_usage as imu
#imu.start_watching_memory()

class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


num = 1024 * 256
x = [ MyClass(1,1) for i in range(num)]
print x[0]

