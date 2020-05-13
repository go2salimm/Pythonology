# python -m SimpleHTTPServer

from pprint import pprint

mydict = {'name':'Tom', 'age': 11, 'personality':'good'}
pprint(mydict)

print mydict


class A(object):
    def __init__(self, a, b, c):
        self.__dict__.update({ k : v for k,v in locals().items() if k!= 'self'})


Ainst = A(10,20,30)

#git commit 3, 4
