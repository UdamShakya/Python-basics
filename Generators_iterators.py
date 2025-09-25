# generators_iterators.py
from typing import Iterator, Generator

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    """Yield first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b

class FibonacciIterator:
    """Custom iterator that produces Fibonacci numbers indefinitely (or until max)."""
    def __init__(self, limit: int = None):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.limit is not None and self.count >= self.limit:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

def running_total():
    """Generator that keeps a running total and accepts 'add' via send()."""
    total = 0
    while True:
        value = (yield total)  # returns current total and waits for next send()
        if value is None:
            continue
        total += value

if __name__ == "__main__":
    print("fibonacci_gen(8):", list(fibonacci_gen(8)))

    print("FibonacciIterator limit=6:", [x for x in FibonacciIterator(limit=6)])

    # demonstrate send()
    gen = running_total()
    print("initial total:", next(gen))   # prime -> yields 0
    print("after sending 5:", gen.send(5))   # total = 5
    print("after sending 3:", gen.send(3))   # total = 8
    gen.close()
