# context_managers_helpers.py
import time
from contextlib import contextmanager

class Timer:
    """Class-based context manager to time a block."""
    def __init__(self, label="Block"):
        self.label = label
        self._start = None

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self._start
        print(f"[TIMER] {self.label} finished in {elapsed:.6f}s")
        # return False to propagate exceptions, True to suppress
        return False

@contextmanager
def open_safe(path, mode="r", encoding="utf-8"):
    """Simple generator-based context manager for safe file open."""
    f = None
    try:
        f = open(path, mode, encoding=encoding)
        yield f
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    with Timer("sleepy"):
        time.sleep(0.2)

    # Use open_safe to write/read a temp file
    path = "temp_demo.txt"
    with open_safe(path, "w") as f:
        f.write("hello context managers\n")

    with open_safe(path, "r") as f:
        print("File contains:", f.read().strip())
