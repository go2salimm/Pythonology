print "\nMap"

items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)

squaredMap = list(map(lambda x: x**2, items))
print "squaredMap = ", squaredMap


def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
def sub(x):
    return (x-0)


funcs = [multiply, add, sub]
for i in range(5):
    value = list(map(lambda x: x(i),funcs))
    print value


print "\nFilter"

number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x <0 , number_list))
print (less_than_zero)


print "\nReduce"
product = 1
list = [1,2,3,4]
for num in list:
    product = product * num
    print product


from functools import reduce
product = reduce((lambda x, y : x*y), list)
print "product using reduce :", product