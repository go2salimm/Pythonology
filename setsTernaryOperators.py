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