targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        targets = [str(value) for value in targets]
        print("|".join(targets))
        break
    tokens = command.split()
    action = tokens[0]
    index = int(tokens[1])
    if action == "Shoot":
        power = int(tokens[2])
        # if the "target" exists
        if len(targets) > index >= 0:
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        value = int(tokens[2])
        if len(targets) > index >= 0:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    else:
        radius = int(tokens[2])
        if index + radius < len(targets) and index - radius >= 0:
            del(targets[index-radius:index+radius+1])
        else:
            print("Strike missed!")