class CustomIterator:
    def __init__(self, sequence: list, start_index, end_index):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index:
            item = self.__sequence[self.__start_index]
            self.__start_index += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6], 2, 4)
    iterator = iter(custom_iterator)
    for item in custom_iterator:
        print(item)