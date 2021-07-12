import os
import pickle
print(os.makedirs("test/data"))


import random

with open("task5_1.text", "a") as file:
        file.write(
            "operations = []
                for _ in range(100):
                    left = random.randint(0, 500)
                    right = random.randint(0, 500)
                    operation = random.randint(1, 3)
                    operations.append((left, right, operation))
                print(operations)
                                \n")

        str_numbers =[]
        with open("task5_1.text", "wb") as file:
            text = picle.dumps(str_numbers)
        file.write(text)

