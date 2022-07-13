students_num = int(input())
students = {}
for i in range(students_num):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = grade
    else:
        students[student] += grade
        students[student] /= 2

for student in students:
    if students[student] >= 4.5:
        print(f"{student} -> {students[student]:.2f}")