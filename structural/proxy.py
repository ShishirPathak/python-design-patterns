"""Pattern: Proxy
Category: Structural
Problem it solves: Controls access to an object, adding a layer of indirection.
When to use: Lazy loading, access control, or logging around an object.
When not to use: Direct access is simple and safe.
"""

class RealService:
    def fetch(self):
        return "data"


class ServiceProxy:
    def __init__(self):
        self._service = None

    def fetch(self):
        if self._service is None:
            self._service = RealService()
        return self._service.fetch()


def demo():
    proxy = ServiceProxy()
    print(proxy.fetch())


if __name__ == "__main__":
    demo()
