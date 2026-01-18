"""Pattern: Template Method
Category: Behavioral
Problem it solves: Defines the skeleton of an algorithm while letting subclasses fill steps.
When to use: You want to reuse a fixed algorithm with variable steps.
When not to use: The algorithm is simple or doesn't vary.
"""

class DataProcessor:
    def process(self):
        data = self.load()
        data = self.transform(data)
        self.save(data)

    def load(self):
        raise NotImplementedError

    def transform(self, data):
        raise NotImplementedError

    def save(self, data):
        raise NotImplementedError


class UppercaseProcessor(DataProcessor):
    def load(self):
        return "hello"

    def transform(self, data):
        return data.upper()

    def save(self, data):
        print(data)


def demo():
    UppercaseProcessor().process()


if __name__ == "__main__":
    demo()
