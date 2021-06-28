friends = ["John", "Marta", "James"]
enamies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend == "James":
        break
    else:
            if friend in enamies:
                print(f"{friend} we are not the best friends anymore")
            else:
                print(f'{friend} we are the best friends')
