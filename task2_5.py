names = ["John Dow", "John Dow", "Marta Dow"]


def get_unique_names(names):
    unique = []

    for name in names:
        if name in unique:
            continue
        else:
            unique.append(name)
    return unique


print(get_unique_names(names))
