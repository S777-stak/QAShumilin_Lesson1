from typing import Union, Callable


def custom_filter(callback: Callable, sequence) -> Union[int, float, str]:
    result = []
    for item in sequence:
        if callback(item):
            result.append(item)
    return result


if __name__ == '__main__':
    print(custom_filter(lambda item: item > 5, [1, 2, 3, 4, 5, 6, 7]))