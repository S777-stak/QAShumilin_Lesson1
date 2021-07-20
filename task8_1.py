def header(func):
    def inner(a, b):
        print(func.__name__)
        print(func(a, b))
    return inner

@header
def sum(a, b):
    return a + b

sum(1, 2)
