import pickle
with open("test/data/file.txt", 'rb') as file:
    operations = pickle.load(file)
for operation in operations:
    left, right, element = operation
    if element == 1:
        print(f"{left} + {right}")
    elif element == 2:
        print(f"{left} * {right}")
    else:
        print(f"{left} / {right}")