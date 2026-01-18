"""Pattern: Prototype
Category: Creational
Problem it solves: Creates new objects by copying an existing instance.
When to use: Object creation is expensive or complex, and cloning is simpler.
When not to use: Object initialization is trivial or deep copy semantics are tricky.
"""

import copy


class Prototype:
    def __init__(self, data):
        self.data = data

    def clone(self):
        return copy.copy(self)


def demo():
    original = Prototype([1, 2, 3])
    clone = original.clone()
    clone.data.append(4)
    print(original.data, clone.data)


if __name__ == "__main__":
    demo()
