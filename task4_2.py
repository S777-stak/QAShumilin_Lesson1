

names = ["John", "Marta", "James", "Amanda", "Marianna"] 
for name in names:
    if not name:
        print("Names".center(50, '*'))
    print(f"{name:>10}")

# Good but I see only solution with f string formatting but does not see any
# solution with string methods
# Also no header in the output but should be some header according to
# requirements
# 2 empty lines in the top of module and too much in the end of module
