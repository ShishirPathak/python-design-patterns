"""Pattern: Command
Category: Behavioral
Problem it solves: Encapsulates a request as an object to parameterize and queue actions.
When to use: You need undo, logging, or deferred execution of commands.
When not to use: Simple direct method calls are enough.
"""

class Command:
    def execute(self):
        raise NotImplementedError


class Light:
    def on(self):
        return "Light on"


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.on()


class Remote:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press(self):
        return self.command.execute()


def demo():
    light = Light()
    remote = Remote()
    remote.set_command(LightOnCommand(light))
    print(remote.press())


if __name__ == "__main__":
    demo()
