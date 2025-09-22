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
