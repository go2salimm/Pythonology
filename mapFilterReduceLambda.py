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
lister = [1,2,3,4]
for num in lister:
    product = product * num
    print product


print "\nLambda"

from functools import reduce
product = reduce((lambda x, y : x*y), lister)
print "product using reduce :", product


add = lambda x, y : x + y
print add(3,5)

a = [(1,2), (4,1), (9,10), (13,-3)]
#a.sort(key=lambda x: x[1])
print a


data = zip(a, lister)
data.sort()
print data

list1, list2 = map(lambda t : list(t), zip(*data))
print "list1 = " , list1
print "list2 = " , list2


print "for .. else"

for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            #print str(n) + "equals" + str(x) + '*' , str(n/x)
            print (n , "equals", x, "*", n/x)
            break
    else:
        print (n, "is a prime number")