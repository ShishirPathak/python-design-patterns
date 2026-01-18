"""Pattern: Observer
Category: Behavioral
Problem it solves: Defines a one-to-many dependency to notify observers of changes.
When to use: Multiple parts of a system need to react to events.
When not to use: Direct calls are simpler and the set of listeners is fixed.
"""

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def set_state(self, state):
        self._state = state
        for obs in self._observers:
            obs.update(self._state)


class Observer:
    def update(self, state):
        raise NotImplementedError


class PrintObserver(Observer):
    def update(self, state):
        print(f"Observed: {state}")


def demo():
    subject = Subject()
    subject.attach(PrintObserver())
    subject.set_state("ready")


if __name__ == "__main__":
    demo()
