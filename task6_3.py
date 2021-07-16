
def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False

    if number == 0:
        return False

    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:
            return False
    return True


if __name__ == '__main__':
    for item in range(2, 999):
        print(is_prime(item))
# Well I suppose something is missing in your code and I getting errors
# -3 points
#     for n in range(3, int(sqrt(number).real) + 1, 2):
# NameError: name 'sqrt' is not defined
