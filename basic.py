# hello.py
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python 🚀")


# variables.py
student_name = "Udam"
age = 21
subjects = ["Math", "Physics", "Computer Science"]

print(f"{student_name} is {age} years old.")
print("Subjects enrolled:")
for subject in subjects:
    print("-", subject)


# math_ops.py
def calculate(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "undefined",
        "power": a ** b,
    }

results = calculate(10, 3)
for operation, result in results.items():
    print(f"{operation.capitalize()}: {result}")
