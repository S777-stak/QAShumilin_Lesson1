with (open("task5_1.text", "rb") as file:
byte_text  = file.read()
    numbers_2 = picle.loads(byte_text)
    print(numbers_2)