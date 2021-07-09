
import os
from typing import BinaryIO

print(os.makedirs("test/data"))

with open("task5_1.text", "a") as file:
    for index in range(100):
        file.write(
            "numbers = [(int(a), int(b), int(c) for i in (range(100)]
                                if c == (a + b):
                                    c = 1,
                                elif:
                                    if c == (a - b):
                                        c = 2,
                                else:
                                    c = 3
                                \n")

        str_numbers =[]

        file: BinaryIO
        with open("task5_1.text", "wb") as file:
            text = picle.dumps(str_numbers)
        file.write(text)

with (open("task5_1.text", "rb") as file:
byte_text  = file.read()
    numbers_2 = picle.loads(byte_text)
    print(numbers_2)