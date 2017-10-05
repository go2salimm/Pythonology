# Iterators and Generators

print "Generators"

def generator_function():
    for i in range(10):
        yield i


for item in generator_function():
    print item ,

gen = generator_function()
print "\nUsing next(gen)"
print(next(gen))


def fibon(n):
    a = b = 1                   # result = []
    for i in range(n):
        yield a                 # result.append(a)
        a, b = b, a + b

print "Fibonacci series"
for x in fibon(10):
    print x ,

print "\nIterators"
mystr = 'Salim'
myiter = iter(mystr)
print(next(myiter))
print(next(myiter))


