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



print "Coroutines"

def grep(pattern):
    print("Searching for ", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print line



search = grep('coroutine')
next(search)

search.send("hello")
search.send("new world ")
search.send("this is coroutines")

search.close()


from functools import lru_cache


