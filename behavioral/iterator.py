"""Pattern: Iterator
Category: Behavioral
Problem it solves: Provides a way to access elements of a collection without exposing its internals.
When to use: You need custom iteration logic.
When not to use: Built-in iteration is sufficient.
"""

class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return NumberIterator(self.numbers)


class NumberIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._numbers):
            raise StopIteration
        value = self._numbers[self._index]
        self._index += 1
        return value


def demo():
    collection = NumberCollection([1, 2, 3])
    for n in collection:
        print(n)


if __name__ == "__main__":
    demo()
