"""Pattern: Builder
Category: Creational
Problem it solves: Separates complex object construction from its representation.
When to use: You need step-by-step construction with different configurations.
When not to use: Objects are simple or only one construction path exists.
"""

class Meal:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return ", ".join(self.items)


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_main(self):
        self.meal.add("burger")
        return self

    def add_side(self):
        self.meal.add("fries")
        return self

    def add_drink(self):
        self.meal.add("soda")
        return self

    def build(self):
        return self.meal


class Director:
    def __init__(self, builder):
        self.builder = builder

    def make_combo(self):
        return self.builder.add_main().add_side().add_drink().build()


def demo():
    builder = MealBuilder()
    director = Director(builder)
    meal = director.make_combo()
    print(meal)


if __name__ == "__main__":
    demo()
