employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())
high_happiness_count = 0

employees_happiness = list(map(lambda x: int(x) * improvement_factor, employees_happiness))

average_happiness = sum(employees_happiness) / len(employees_happiness)

filtered = list(filter(lambda employee: employee >= average_happiness, employees_happiness))

if len(employees_happiness) >= len(filtered) / 2:
    print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are not happy!")