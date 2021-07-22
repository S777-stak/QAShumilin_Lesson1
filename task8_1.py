def header(func):
    def inner(a, b):
        print(func.__name__)
        print(func(a, b))
    return inner

@header
def sum(a, b):
    return a + b

sum(1, 2)

# Well nice but your decorator brake logic of your function.

result = sum(5, 6)
print(result)
# Expected result = 11
# Actual result = None
# Decorator should be change main logic of function.
# - 3 points
