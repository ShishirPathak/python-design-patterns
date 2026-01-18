"""Pattern: Adapter
Category: Structural
Problem it solves: Allows incompatible interfaces to work together.
When to use: You need to integrate existing code with a new interface.
When not to use: You can change the existing class directly.
"""

class LegacyPrinter:
    def print_text(self, text):
        return f"Legacy: {text}"


class Printer:
    def print(self, text):
        raise NotImplementedError


class PrinterAdapter(Printer):
    def __init__(self, legacy):
        self.legacy = legacy

    def print(self, text):
        return self.legacy.print_text(text)


def demo():
    legacy = LegacyPrinter()
    adapter = PrinterAdapter(legacy)
    print(adapter.print("hello"))


if __name__ == "__main__":
    demo()
