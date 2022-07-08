searched_course = input()
students_info_dict = {}
while True:
    students_info = searched_course.split(":")

    name = students_info[0]
    student_id = students_info[1]
    course = students_info[2]

    if course not in students_info_dict:
        students_info_dict[course] = []
    students_info_dict[course].append({name: student_id})

    searched_course = input()
    if "_" in searched_course:
        tokens = searched_course.split("_")
        searched_course = " ".join(tokens)
    if searched_course in students_info_dict:
        break

for student in students_info_dict[searched_course]:
    for name in student:
        print(f"{name} - {student[name]}")