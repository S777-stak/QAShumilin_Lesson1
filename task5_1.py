import random
import pickle
import os

os.makedirs("test/data")

list_of_tuples = []
for _ in range(100):
    left = random.randint(1, 100)
    right = random.randint(1, 100)
    operation = random.randint(1, 3)
    list_of_tuples.append((left, right, operation))

print(list_of_tuples)

with open("test/data/file.txt", "wb") as file:
    pickle.dump(list_of_tuples, file)

