numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for index, value in enumerate(numbers):
    if index % 2 != 0:
        b = (index, value)
        print(b)
    else:
        c = (index, value)
        print(c)
