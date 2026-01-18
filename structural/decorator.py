"""Pattern: Decorator
Category: Structural
Problem it solves: Adds behavior to objects dynamically without changing their class.
When to use: You want to extend functionality at runtime.
When not to use: Simple inheritance or direct changes are sufficient.
"""

class Notifier:
    def send(self, message):
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email: {message}"


class NotifierDecorator(Notifier):
    def __init__(self, wrappee):
        self.wrappee = wrappee

    def send(self, message):
        return self.wrappee.send(message)


class SMSDecorator(NotifierDecorator):
    def send(self, message):
        base = super().send(message)
        return f"{base} + SMS"


def demo():
    notifier = SMSDecorator(EmailNotifier())
    print(notifier.send("hi"))


if __name__ == "__main__":
    demo()
