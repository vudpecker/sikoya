"""nested list"""

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_record = {"name": name, "score": score}
    students.append(student_record)

#grades = [student["score"] for student in students]
grades = set([student["score"] for student in students])

if len(grades) == 1:
    print("All students have the same grade.")    


sorted_grades = sorted([student["score"] for student in students])

# Find the second-lowest grade (ignoring the lowest)
second_lowest_grade = sorted_grades[1] if len(sorted_grades) > 1 else None

# Find students with the second-lowest grade
second_lowest_students = [
    student["name"] for student in students if student["score"] == second_lowest_grade
]

# Sort student names alphabetically
second_lowest_students.sort()

if second_lowest_students:
    print("Students with the second-lowest grade:")
    for student in second_lowest_students:
        print(student)
else:
    print("There are no students with the second-lowest grade.")