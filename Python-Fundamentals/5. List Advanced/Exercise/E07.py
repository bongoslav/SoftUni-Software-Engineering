numbers_list = list(map(int, input().split(", ")))
max_value = max(numbers_list)

tens = 10

for group_range in range(10, max_value + 10, 10):
    numbers_in_current_tens = []
    for number in numbers_list[::-1]:
        if number <= group_range:
            numbers_list.remove(number)
            numbers_in_current_tens.insert(0, number)
    print(f"Group of {tens}'s: {numbers_in_current_tens}")
    tens += 10