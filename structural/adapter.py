"""Pattern: Adapter
Category: Structural
Problem it solves: Allows incompatible interfaces to work together.
When to use: You need to integrate existing code with a new interface.
When not to use: You can change the existing class directly.
"""

class LegacyPrinter:
    def print_text(self, text):
        return f"legacy: {text}"

class Printer:
    def print(self, text):
        raise NotImplementedError
    
class AdapterLegacy(Printer):
    def __init__(self, legacy):
        self.legacy = legacy
        
    def print(self, text):
        self.legacy.print_text(text)
        

def demo():
    legacy = LegacyPrinter()
    adapter =AdapterLegacy(legacy)
    print(adapter.print("Hello"))   

if __name__ == "__main__":
    demo()
    