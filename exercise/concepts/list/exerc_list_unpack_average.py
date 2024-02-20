
n = int(input())
student_marks = {}
for _ in range(n):
    
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

if query_name in student_marks:
    marks = student_marks[query_name]
    
    #for mark in marks:
    total = sum(marks)
    average = total/len(marks)
    #print(round(average,3))
    print(f"{average:.2f}")
    
else:
    print("Student not found.")
    
    name, age, section = input().split()
"""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

if query_name in student_marks:
    marks = student_marks[query_name]
    # Calculate average
    total = sum(marks)
    average = total / len(marks)

    # Print the average with two decimal places
    print(f"Average mark for {query_name}: {round(average, 2)}")

else:
    print("Student not found.")
"""