"""Pattern: Bridge
Category: Structural
Problem it solves: Separates abstraction from implementation so they can vary independently.
When to use: You want to mix and match abstractions and implementations.
When not to use: There is only one implementation and no need for flexibility.
"""

class Renderer:
    def render(self, shape_name):
        raise NotImplementedError


class RasterRenderer(Renderer):
    def render(self, shape_name):
        return f"Raster {shape_name}"


class VectorRenderer(Renderer):
    def render(self, shape_name):
        return f"Vector {shape_name}"


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        return self.renderer.render("circle")


def demo():
    for renderer in (RasterRenderer(), VectorRenderer()):
        shape = Circle(renderer)
        print(shape.draw())


if __name__ == "__main__":
    demo()
