print "Sets"
some_list = ['a', 'b', 'c', 'd', 'a', 'c', 'm']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print "No Duplicates : " , duplicates


print "Intersection"
firstSet = set(['yellow', 'red', 'brown', 'green', 'black'])  # create first set
secondSet = {'red', 'blue', 'green', 'white'}                 # create second set
print (secondSet.intersection(firstSet))

print "Difference"
print(secondSet.difference(firstSet))


print "TernaryOperators"
condition = True
state = "True" if condition else "False"
print state

condition = False
state = "True" if condition else "False"
print state


my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 3))
print counter_list


print id(counter_list)
print id(condition)


import inspect
print inspect.getmembers(str)

input_list = [2,3,4,5,6,7,8,9]
lvariable = [ x for x in input_list if x%2==0]
print lvariable

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
svariable = { x for x in input_list if x%2==0 }
print svariable


try:
    file = open('/tmp/out.log', 'rb')
except EOFError as e:
    print "An EOFError occured. {}".format(e.args[-1])
    raise e
except IOError as e:
    print "An IOError occured. {}".format(e.args[-1])
    #raise e
except Exception:
    raise
else:
    print "This will only run if no exception occurs"
finally:
    print "This will be printed whether or not an exception occured!"