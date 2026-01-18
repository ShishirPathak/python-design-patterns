"""Pattern: State
Category: Behavioral
Problem it solves: Allows an object to change behavior when its internal state changes.
When to use: Behavior depends on state and transitions are explicit.
When not to use: A few if/else branches are enough.
"""

class State:
    def handle(self, context):
        raise NotImplementedError


class StateA(State):
    def handle(self, context):
        context.state = StateB()
        return "A -> B"


class StateB(State):
    def handle(self, context):
        context.state = StateA()
        return "B -> A"


class Context:
    def __init__(self):
        self.state = StateA()

    def request(self):
        return self.state.handle(self)


def demo():
    context = Context()
    print(context.request())
    print(context.request())


if __name__ == "__main__":
    demo()
