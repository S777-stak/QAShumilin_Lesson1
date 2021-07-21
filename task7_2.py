from typing import Union, Callable


def custom_map(callback: Callable, sequence) -> Union[int, float, str]:
    result = []
    for item in sequence:
        if callback(item):
            result.append(item)
    return result


if __name__ == '__main__':
    print(custom_map(lambda item: item * 2, [1, 2, 3, 4, 5, 6, 7]))

# This map does not modify anything. As you can see I am trying to
# multiple on 2 each item from you list.
# But inside custom map you just call this callback. But callback for map
# always should return modified item instead of True or False and you should
# just place this new modified item into the new sequence
# -5 points
