# Flyweight Pattern Example in Python
"""Pattern: Flyweight
Category: Structural
Problem it solves: Reduces memory usage by sharing common parts of objects.
When to use: You have a large number of similar objects that can share data.
When not to use: Objects are unique and cannot share data.
"""

#Flyweight (shared)

class Circle:
    def __init__(self,color):
        self.color = color
    def draw(self,x,y):
        print(f"Circle {self.color} at {x},{y}")

# Factory
class CircleFactory:
    _cache = {}
    
    @classmethod
    def get_circle(cls, color):
        if color not in cls._cache:
            cls._cache[color] = Circle(color)
        
        return cls._cache[color]

# Extrinsic state holder (client-side)
class PositionedCircle:
    def __init__(self, circle, x , y):
        self.circle = circle # shared flyweight
        self.x = x          # extrinsic
        self.y = y          # extrinsic
    def draw(self):
        self.circle.draw(self.x, self.y)
        
def demo():
    red_circle = CircleFactory.get_circle("Red")
    
    c1 = PositionedCircle(red_circle, 10, 20)
    c2 = PositionedCircle(red_circle, 50, 70)
    
    c1.draw()
    c2.draw()

if __name__ == '__main__':
    demo()