from typing import Union, Callable

def custom_reduce(callback: Callable, sequence) -> Union[int, float, str]:
    result = []
    for item in sequence:
        if callback(item):
            result.append(item.__add__(2))  # using magic method not neaded here at all
    return result


if __name__ == '__main__':
    print(custom_reduce(lambda a, b: a + b, [1, 2, 3, 4, 5, 6, 7]))

# Well same thing. lambda item: item - this lambda will not do anything but
# should reduce results and return it.
# main idea is to call callback and feed 2 arguments until arguments end.
# -5 points
