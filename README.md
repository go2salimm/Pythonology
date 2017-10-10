# Pythonology

git clone https://github.com/go2salimm/Pythonology.git

# Debugging
pdb.set_trace()
Commands:
    c: continue execution
    w: shows the context of the current line it is executing.
    a: print the argument list of the current function
    s: Execute the current line and stop at the first possible occasion.
    n: Continue execution until the next line in the current function is reached or it returns.

# Generators
an iterator is an object that enables a programmer to traverse a container, particularly lists. 
iterable -->  __iter__ or __getitem__ 
iterator -->  next or __next__
iteration --> looping 
Generators are iterators.  You iterate over them once.  They generate the values on the fly and yield.


# Map, Filter and Reduce
map applies a function to all the items in the inputlist:  map(function_to_apply, list_of_inputs)
filter creates a list of elements for which a function returns true
reduce is a useful function for performing computation on a list and returning the result

# set
Sets behave mostly like lists but they cannot contain duplicate values.

# decorators
Decorators let you execute code before and after a function. 
Decorators wrap a function and modify its behavior
eg. def a_new_decorator(func):
    @a_new_decorator
    def b_func()   
 equals b_func = a_new_decorator(b_func)


# References :
Intermediate Python Learning - http://book.pythontips.com/en/latest





