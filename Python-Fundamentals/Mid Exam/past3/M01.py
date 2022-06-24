students_per_hour1 = int(input())
students_per_hour2 = int(input())
students_per_hour3 = int(input())
students_count = int(input())

total_students_per_hour = students_per_hour1 + students_per_hour2 + students_per_hour3
hours = 0
while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= total_students_per_hour

print(f"Time needed: {hours}h.")