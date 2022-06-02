n = int(input())

numbers_list = []
for _ in range(n):
    number = int(input())
    numbers_list.append(number)

command = input()
if command == "even":
    for num in numbers_list[::-1]:
        if num % 2 != 0:
            numbers_list.remove(num)
elif command == "odd":
    for num in numbers_list[::-1]:
        if num % 2 == 0:
            numbers_list.remove(num)
elif command == "negative":
    for num in numbers_list[::-1]:
        if num >= 0:
            numbers_list.remove(num)
elif command == "positive":
    for num in numbers_list[::-1]:
        if num < 0:
            numbers_list.remove(num)

print(numbers_list)