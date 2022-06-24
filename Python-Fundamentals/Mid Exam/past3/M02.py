numbers = list(map(int, input().split()))

command = input()

while command != "end":
    tokens = command.split()
    action = tokens[0]
    if action == "swap":
        index1 = int(tokens[1])
        index2 = int(tokens[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        index1 = int(tokens[1])
        index2 = int(tokens[2])
        numbers[index1] = numbers[index1] * numbers[index2]
    elif action == "decrease":
        numbers = [value - 1 for value in numbers]

    command = input()
numbers = [str(value) for value in numbers]
print(", ".join(numbers))