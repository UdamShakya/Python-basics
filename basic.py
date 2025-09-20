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


# grading.py
score = int(input("Enter your exam score: "))

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")

students = {
    "Alice": [85, 90, 92],
    "Bob": [70, 65, 80],
    "Charlie": [95, 100, 98],
}

for student, marks in students.items():
    avg = sum(marks) / len(marks)
    status = "Pass" if avg >= 50 else "Fail"
    print(f"{student} → Average: {avg:.2f}, Status: {status}")

count = 0
while count < 3:
    print("While loop demo:", count)
    count += 1