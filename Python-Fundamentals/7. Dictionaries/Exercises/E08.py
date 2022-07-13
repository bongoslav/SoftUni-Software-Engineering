entry = input()
courses_info = {}
while entry != "end":
    course, student = entry.split(" : ")
    if course not in courses_info:
        courses_info[course] = []
    courses_info[course].append(student)

    entry = input()

for course, students in courses_info.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")