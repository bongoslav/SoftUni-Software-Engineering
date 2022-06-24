numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
average = sum(numbers) / len(numbers)

greater_than_average = []
for number in numbers:
    if number > average:
        if len(greater_than_average) < 5:
            greater_than_average.append(number)

if len(greater_than_average) == 0:
    print("No")
else:
    print(" ".join(str(x) for x in greater_than_average))