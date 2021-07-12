import pickle
with open("test/data/file.txt", 'rb') as file:
    operations = pickle.load(file)
for operation in operations:
    operation = (left, right, operation)
    if operation == 1:
        print('left' + 'right')
    elif operation == 2:
        print('left' * 'right')
    else:
        print('left' / 'right')