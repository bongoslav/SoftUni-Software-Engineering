values = list(map(int, input().split()))

count = 0
command = input()
while command != "End":
    index = int(command)

    if index < len(values):
        count += 1
        current_value = values[index]
        values[index] = -1

        for value_index in range(len(values)):
            if values[value_index] == -1:
                continue
            elif values[value_index] > current_value:
                values[value_index] -= current_value
            else:
                values[value_index] += current_value

    command = input()

values = [str(value) for value in values]
print(f"Shot targets: {count} -> {' '.join(values)}")