"""Pattern: Composite
Category: Structural
Problem it solves: Treats individual objects and compositions uniformly.
When to use: You need tree structures with uniform operations.
When not to use: Objects don't naturally form a hierarchy.
"""

from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self):
        pass
    
    @abstractmethod
    def print_structure(self,indent=0):
        pass
    
    @abstractmethod
    def delete():
        pass

class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
    def print_structure(self, indent=0):
        return (f"{' ' * indent}- File: {self.name} (Size: {self.size}KB)")
    
    def delete(self):
        return f"File {self.name} deleted."

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item: FileSystemItem):
        self.items.append(item)
    
    def get_size(self):
        total_size = sum(item.get_size() for item in self.items)
        return total_size
    
    def print_structure(self, indent=0):
        structure = [f"{' ' * indent}+ Folder: {self.name}"]
        for item in self.items:
            structure.append(item.print_structure(indent + 2))
        return "\n".join(structure)
    
    def delete(self):
        for item in self.items:
            item.delete()
        return f"Folder {self.name} and all its contents deleted."   
    
class FileSystemDemo:
    file1 = File("file1.txt", 10)
    file2 = File("file2.txt", 20)
    file3 = File("file3.txt", 30)
    
    folder1 = Folder("folder1")
    folder1.add_item(file1)
    folder1.add_item(file2)
    
    folder2 = Folder("folder2")
    folder2.add_item(file3)
    folder2.add_item(folder1)
    
    print("Structure:\n", folder2.print_structure())
    print("Total Size:", folder2.get_size(), "KB")
    print(folder2.delete())
    
if __name__ == "__main__":   
    FileSystemDemo()     
