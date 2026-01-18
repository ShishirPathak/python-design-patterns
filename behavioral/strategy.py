"""Pattern: Strategy
Category: Behavioral
Problem it solves: Encapsulates interchangeable algorithms behind a common interface.
When to use: You need to switch behavior at runtime.
When not to use: Only one algorithm is needed.
"""

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy(data)


def demo():
    upper = lambda s: s.upper()
    lower = lambda s: s.lower()
    context = Context(upper)
    print(context.execute("Hello"))
    context.strategy = lower
    print(context.execute("Hello"))


if __name__ == "__main__":
    demo()
