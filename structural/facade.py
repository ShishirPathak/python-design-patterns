"""Pattern: Facade
Category: Structural
Problem it solves: Provides a simplified interface to a complex subsystem.
When to use: You want to hide complexity behind a simple API.
When not to use: The subsystem is already simple or needs full control.
"""

class CPU:
    def start(self):
        return "CPU started"


class Memory:
    def load(self):
        return "Memory loaded"


class Disk:
    def read(self):
        return "Disk read"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = Disk()

    def start(self):
        return ", ".join([self.cpu.start(), self.memory.load(), self.disk.read()])


def demo():
    computer = ComputerFacade()
    print(computer.start())


if __name__ == "__main__":
    demo()
