
n = int(input())

students = []
for _ in range(n):
    name, age, section = input("Enter student name, age, and section (space-separated): ").split()
    students.append([name, int(age), section]) 
#Printing
for student in students:
    name, age, section = student  # Unpack the tuple
    print(f"Name: {name}, Age: {age}, Section: {section}")
"""
target_name = input("Enter the name of the student to find their age: ")

found = False
for student in students:
    name, age, section = student
    if name == target_name:
        print(f"Age of {name}: {age}")
        found = True
        break  # Stop searching after finding the name

if not found:
  print(f"Student with name '{target_name}' not found.")
"""