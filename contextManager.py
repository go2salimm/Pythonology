
file = open("/tmp/CMFile.txt", "w")
try:
    file.write('hello\n')
finally:
    file.close()


# equals:


with open("/tmp/CMFile.txt", "a") as opened_file:
    opened_file.write("Hello World")



class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()


with File('/tmp/demo.txt', 'w') as opened_file:
    opened_file.write("Hola World")


with File('/tmp/demo.txt', 'w') as opened_file:
    opened_file.undefined_function()



from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()