"""Pattern: Factory Method
Category: Creational
Problem it solves: Creates objects without specifying the exact class of object to create.
When to use: Subclasses decide which class to instantiate.
When not to use: Object creation is simple and unlikely to change.
"""

class Product:
    def use(self):
        raise NotImplementedError


class ConcreteProductA(Product):
    def use(self):
        return "Product A"


class ConcreteProductB(Product):
    def use(self):
        return "Product B"


class Creator:
    def factory_method(self):
        raise NotImplementedError

    def operation(self):
        product = self.factory_method()
        return f"Creator uses {product.use()}"


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


def demo():
    for creator in (ConcreteCreatorA(), ConcreteCreatorB()):
        print(creator.operation())


if __name__ == "__main__":
    demo()
