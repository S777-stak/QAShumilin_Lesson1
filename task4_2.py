

names = ["John", "Marta", "James", "Amanda", "Marianna"] 
for name in names:
    if not name:
        print("Names".center(50, '*'))
    print(f"{name:>10}")

