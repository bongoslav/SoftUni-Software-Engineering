coffees = input().split()
commands_count = int(input())

for count in range(commands_count):
    command = input()
    tokens = command.split()
    action = tokens[0]
    if action == "Include":
        coffee_to_add = tokens[1]
        coffees.append(coffee_to_add)
    elif action == "Remove":
        num_coffees = int(tokens[2])
        if num_coffees < len(coffees):
            if tokens[1] == "first":
                del coffees[:num_coffees]
            else:
                del coffees[-num_coffees:]
    elif action == "Prefer":
        coffee_index1 = int(tokens[1])
        coffee_index2 = int(tokens[2])
        if 0 <= coffee_index1 < len(coffees) - 1 and 0 <= coffee_index2 < len(coffees) - 1:
            coffees[coffee_index1], coffees[coffee_index2] = coffees[coffee_index2], coffees[coffee_index1]
    else:
        coffees.reverse()

print(f"Coffees:\n{' '.join(coffees)}")