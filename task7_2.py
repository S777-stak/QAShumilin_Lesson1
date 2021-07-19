from typing import Union, Callable


def custom_map(callback: Callable, sequence) -> Union[int, float, str]:
    result = []
    for item in sequence:
        if callback(item):
            result.append(item*5)
    return result


if __name__ == '__main__':
    print(custom_map(lambda item: item, [1, 2, 3, 4, 5, 6, 7]))