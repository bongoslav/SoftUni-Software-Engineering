numbers = list(map(int, input().split(", ")))

even_indices = [index for index, number in enumerate(numbers) if number % 2 == 0]

print(even_indices)