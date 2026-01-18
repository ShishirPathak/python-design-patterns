"""Pattern: Abstract Factory
Category: Creational
Problem it solves: Creates families of related objects without specifying their concrete classes.
When to use: You need to swap entire product families consistently.
When not to use: Only a few objects are needed and families are unlikely to change.
"""

class AbstractProductA:
    def feature_a(self):
        raise NotImplementedError


class AbstractProductB:
    def feature_b(self):
        raise NotImplementedError


class ConcreteProductA1(AbstractProductA):
    def feature_a(self):
        return "A1"


class ConcreteProductA2(AbstractProductA):
    def feature_a(self):
        return "A2"


class ConcreteProductB1(AbstractProductB):
    def feature_b(self):
        return "B1"


class ConcreteProductB2(AbstractProductB):
    def feature_b(self):
        return "B2"


class AbstractFactory:
    def create_a(self):
        raise NotImplementedError

    def create_b(self):
        raise NotImplementedError


class Factory1(AbstractFactory):
    def create_a(self):
        return ConcreteProductA1()

    def create_b(self):
        return ConcreteProductB1()


class Factory2(AbstractFactory):
    def create_a(self):
        return ConcreteProductA2()

    def create_b(self):
        return ConcreteProductB2()


def demo():
    for factory in (Factory1(), Factory2()):
        a = factory.create_a()
        b = factory.create_b()
        print(a.feature_a(), b.feature_b())


if __name__ == "__main__":
    demo()
