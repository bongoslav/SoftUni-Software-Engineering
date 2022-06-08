numbers = list(map(int, input().split(", ")))

for number in numbers:
    if number == 0:
        numbers.remove(number)
        numbers.append(number)

print(numbers)