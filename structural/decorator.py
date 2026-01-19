"""Pattern: Decorator
Category: Structural
Problem it solves: Adds behavior to objects dynamically without changing their class.
When to use: You want to extend functionality at runtime.
When not to use: Simple inheritance or direct changes are sufficient.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

#1 component (interface)
class Component(ABC):
    @abstractmethod
    def execute(self):
        pass

#2 ConcreteComponent (core behaviour)

class ConcreteComponent(Component):
    def execute(self):
        return "core"
    
#3 BaseDecorator (is-a compnent , has-a component)
class BaseDecorator(Component):
    def __init__(self, wrapped: Component):
        self.wrapped = wrapped # has-a relationship
        
    def execute(self):
        return self.wrapped.execute()
        

#4 ConcreteDecorator A (adds behavior)
class ConcreteDecoratorA(BaseDecorator):
    def execute(self):
        before = "A(before)"
        core = super().execute()
        after = "A(after)"
        return f"{before} -> {core} -> {after} "
    
#4 ConcreteDecorator B (adds behavior)
class ConcreteDecoratorB(BaseDecorator):
    def execute(self):
        core = super().execute()
        return f"{core} + B(extra) "
    
    def otherMethod(self):
        return "B Specific method"

class demo():
    base = ConcreteComponent()
    print("Base:", base.execute())
    
    # wrap base with A
    a = ConcreteDecoratorA(base)
    print("A(base)", a.execute())

    # stack decorators: A wraps B wraps base
    stacked = ConcreteDecoratorA(ConcreteDecoratorB(base))
    print("A(b(base))", stacked.execute())
    
if __name__ == "__main__":   
    demo()
    