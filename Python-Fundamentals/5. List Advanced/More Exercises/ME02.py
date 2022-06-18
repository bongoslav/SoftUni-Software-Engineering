message = input()

numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []

for char in message:
    if char.isdigit():
        numbers_list.append(char)
    else:
        non_numbers_list.append(char)

for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

result = ""
for num_taken, num_skipped in zip(take_list, skip_list):
    if int(num_taken) == 0:
        result += ""
    else:
        for i in range(int(num_taken)):
            added_letter = non_numbers_list[i]
            result += added_letter
    non_numbers_list[:int(num_taken)] = []
    if int(num_skipped) == 0:
        pass
    else:
        non_numbers_list[:int(num_skipped)] = []

print(result)