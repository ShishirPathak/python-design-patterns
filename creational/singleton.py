"""Pattern: Singleton
Category: Creational
Problem it solves: Ensures a class has only one instance and provides a global access point.
When to use: You need a single shared instance (e.g., config, logger) across the app.
When not to use: When global state makes testing or concurrency harder, or multiple instances are fine.
"""

class Singleton:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
        return cls._instance


def demo():
    a = Singleton("first")
    b = Singleton("second")
    print(a is b)
    print(a.name, b.name)


if __name__ == "__main__":
    demo()
