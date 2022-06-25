groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    tokens = command.split()
    action = tokens[0]
    item = tokens[1]

    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
    elif action == "Correct":
        old_item = item
        new_item = tokens[2]
        if old_item in groceries:
            old_item_index = groceries.index(old_item)
            groceries[old_item_index] = new_item
    else:
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    command = input()

print(", ".join(groceries))