numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for index, value in enumerate(numbers):
    if index % 2 != 0:
        b = (index, value)
        print(b)
    else:
        c = (index, value)
        print(c)
# Good but you should split you existing numbers list on 2 different list of tuples.
# All odd indexes with values should be placed in odd_items list and all even in even_items list.
