def some(args):
    pass


def header(str):
    def midleware_dec(func):
        def inner(some):
            str = func.__name__

        return f"{func(some)}\n{header}"

        return inner

    return midleware_dec


@header(str)
def sum(a, b):
    return a + b


print(sum(2, 3))