"""Pattern: Composite
Category: Structural
Problem it solves: Treats individual objects and compositions uniformly.
When to use: You need tree structures with uniform operations.
When not to use: Objects don't naturally form a hierarchy.
"""

class Component:
    def operation(self):
        raise NotImplementedError


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return self.name


class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        parts = [child.operation() for child in self.children]
        return f"{self.name}({', '.join(parts)})"


def demo():
    root = Composite("root")
    root.add(Leaf("a"))
    branch = Composite("branch")
    branch.add(Leaf("b"))
    root.add(branch)
    print(root.operation())


if __name__ == "__main__":
    demo()
