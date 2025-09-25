# decorators_advanced.py
import functools
import time
import random

def logger(func):
    """Simple logger decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    """Measure execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] {func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

def retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Retry decorator with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _retries, _delay = retries, delay
            last_exc = None
            for attempt in range(1, _retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"[RETRY] attempt {attempt} failed: {e}. retrying in {_delay}s...")
                    time.sleep(_delay)
                    _delay *= backoff
            raise last_exc
        return wrapper
    return decorator

# Example usage
@logger
@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

@retry(retries=4, delay=0.5, backoff=1.5)
def flaky_action():
    """Simulate an unreliable function."""
    if random.random() < 0.7:
        raise RuntimeError("Temporary failure")
    return "success"

if __name__ == "__main__":
    print("slow_add result:", slow_add(3, 4))
    try:
        print("flaky_action:", flaky_action())
    except Exception as e:
        print("flaky_action final error:", e)
