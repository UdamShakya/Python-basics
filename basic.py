# # hello.py
# name = input("What is your name? ")
# print(f"Hello, {name}! Welcome to Python 🚀")


# # variables.py
# student_name = "Udam"
# age = 21
# subjects = ["Math", "Physics", "Computer Science"]

# print(f"{student_name} is {age} years old.")
# print("Subjects enrolled:")
# for subject in subjects:
#     print("-", subject)


# # math_ops.py
# def calculate(a, b):
#     return {
#         "addition": a + b,
#         "subtraction": a - b,
#         "multiplication": a * b,
#         "division": a / b if b != 0 else "undefined",
#         "power": a ** b,
#     }

# results = calculate(10, 3)
# for operation, result in results.items():
#     print(f"{operation.capitalize()}: {result}")


# # grading.py
# score = int(input("Enter your exam score: "))

# if score >= 90:
#     grade = "A"
# elif score >= 75:
#     grade = "B"
# elif score >= 60:
#     grade = "C"
# elif score >= 40:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Your grade is {grade}")

# students = {
#     "Alice": [85, 90, 92],
#     "Bob": [70, 65, 80],
#     "Charlie": [95, 100, 98],
# }

# for student, marks in students.items():
#     avg = sum(marks) / len(marks)
#     status = "Pass" if avg >= 50 else "Fail"
#     print(f"{student} → Average: {avg:.2f}, Status: {status}")

# count = 0
# while count < 3:
#     print("While loop demo:", count)
#     count += 1

#     # functions_files.py

# def save_student_grade(name, scores, filename="grades.txt"):
#     avg = sum(scores) / len(scores)
#     grade = (
#         "A" if avg >= 90 else
#         "B" if avg >= 75 else
#         "C" if avg >= 60 else
#         "D" if avg >= 40 else
#         "F"
#     )
    
#     result = f"{name}: {avg:.2f} ({grade})\n"
    
#     # Write to file
#     with open(filename, "a") as file:
#         file.write(result)
    
#     return result

# # Example usage
# students = {
#     "Alice": [85, 90, 92],
#     "Bob": [70, 65, 80],
#     "Charlie": [95, 100, 98],
# }

# for student, marks in students.items():
#     print(save_student_grade(student, marks))


#     # Exception Handling Example

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# except ValueError:
#     print("Error: Please enter valid integers!")

# finally:
#     print("Program finished.")


# # Functions Example

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Test
# print("Factorial of 5:", factorial(5))
# print("Is 17 prime?", is_prime(17))

# # Custom math module

# def square(n):
#     return n * n

# def cube(n):
#     return n * n * n


# # Using the custom math module

# import math_utils

# print("Square of 4:", math_utils.square(4))
# print("Cube of 3:", math_utils.cube(3))


# # Basic Car Class Example

# class Car:
#     def __init__(self, brand, speed=0):
#         self.brand = brand
#         self.speed = speed

#     def accelerate(self, value):
#         self.speed += value
#         print(f"{self.brand} accelerated. Speed: {self.speed} km/h")

#     def brake(self, value):
#         self.speed = max(0, self.speed - value)
#         print(f"{self.brand} slowed down. Speed: {self.speed} km/h")

# # Test
# my_car = Car("Toyota")
# my_car.accelerate(30)
# my_car.brake(10)

# # Inheritance Example

# class Car:
#     def __init__(self, brand, speed=0):
#         self.brand = brand
#         self.speed = speed

#     def accelerate(self, value):
#         self.speed += value
#         print(f"{self.brand} accelerated. Speed: {self.speed} km/h")

#     def brake(self, value):
#         self.speed = max(0, self.speed - value)
#         print(f"{self.brand} slowed down. Speed: {self.speed} km/h")

# class ElectricCar(Car):
#     def __init__(self, brand, battery_capacity, speed=0):
#         super().__init__(brand, speed)
#         self.battery_capacity = battery_capacity

#     def charge(self):
#         print(f"{self.brand} is charging... Battery: {self.battery_capacity} kWh")

# # Test
# tesla = ElectricCar("Tesla", 75)
# tesla.accelerate(50)
# tesla.brake(20)
# tesla.charge()


# Simple Contact Book Project

class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename

    def add_contact(self, name, phone):
        with open(self.filename, "a") as file:
            file.write(f"{name},{phone}\n")
        print(f"Contact {name} added.")

    def view_contacts(self):
        try:
            with open(self.filename, "r") as file:
                contacts = file.readlines()
                if not contacts:
                    print("No contacts found.")
                    return
                for contact in contacts:
                    name, phone = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}")
        except FileNotFoundError:
            print("No contacts file found yet.")

    def search_contact(self, name):
        try:
            with open(self.filename, "r") as file:
                contacts = file.readlines()
                for contact in contacts:
                    cname, phone = contact.strip().split(",")
                    if cname.lower() == name.lower():
                        print(f"Found: {cname} - {phone}")
                        return
                print("Contact not found.")
        except FileNotFoundError:
            print("No contacts file found yet.")

# Test
book = ContactBook()
book.add_contact("Alice", "12345")
book.add_contact("Bob", "67890")
book.view_contacts()
book.search_contact("Alice")

# oop_dataclass_encapsulation.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    hobbies: List[str] = field(default_factory=list)

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = float(balance)  # "private" attribute by convention

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __repr__(self) -> str:
        return f"<BankAccount owner={self.owner!r} balance={self._balance:.2f}>"

if __name__ == "__main__":
    # dataclass usage
    alice = Person("Alice", 25, hobbies=["boxing", "coding"])
    print(alice.greet())

    # bank account usage
    acct = BankAccount("Udam", 100.0)
    print(acct)
    acct.deposit(50)
    print("After deposit:", acct.balance)
    try:
        acct.withdraw(200)
    except ValueError as e:
        print("Withdraw error:", e)

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
