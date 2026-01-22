"""Pattern: Proxy
Category: Structural
Problem it solves: Controls access to an object, adding a layer of indirection.
When to use: Lazy loading, access control, or logging around an object.
When not to use: Direct access is simple and safe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import time

# 1) Subject (interface)
class Image(ABC):
    @abstractmethod
    def display(self) ->str:
        pass

# 2) Real Subject(expensive / heavy)

class RealImage(Image):
    def __init__(self, filename:str):
        self.filename = filename
        self._load_from_disk()
    
    def _load_from_disk(self):
        # simulate heavy work (disk/network/ etc..)
        
        print(f"[RealImage] loading '{self.filename}' from disk(slow)")
        time.sleep(2)
    
    def display(self):
        return f"[RealImage] Displaying '{self.filename}'"

# 3) Proxy (controls access, lazy-loading, cache, logs)

class ImageProxy(Image):
    def __init__(self, filename:str):
        self.filename = filename
        self._real_image: RealImage | None = None
        self._cached_display : str | None = None
        self.result: str | None = None
    
    def display(self) -> str:
        start = time.time()
        print(f"[Proxy] display() called for '{self.filename}'")
        
        # caching proxy behavior
        if self._cached_display is not None:
            self.result = self._cached_display
            print("[Proxy] returning cached result (fast). ")       
        else:
             # virtual proxy behavior (lazy load)
             if self._real_image is None:
                print("[Proxy] RealImage not created yet. Creating now...")
                self._real_image = RealImage(self.filename)
                self.result = self._real_image.display()
                self._cached_display = self.result
                
        
        elapsed_ms = (time.time() - start) * 1000
        print(f"[Proxy] display() took {elapsed_ms:.1f} ms")
        
        return self.result
                     
def demo():
    print("=== Client uses Image interface ===")
    img: Image = ImageProxy("cat.png")
    
    print("\n--- First call (should be slow: loads real object) ---")
    print(img.display())
    
    print("\n--- second call (should be fast: cached) ---")
    print(img.display())

if __name__ == "__main__":
    demo()
