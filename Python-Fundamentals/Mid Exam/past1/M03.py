elements = input().split()

command = input()
moves = 0
while command != "end" and len(elements) > 0:
    moves += 1
    index1 = int(command.split()[0])
    index2 = int(command.split()[1])

    if index1 == index2 or index1 >= len(elements) or index1 < 0 or index2 >= len(elements) or index2 < 0:
        elements.insert(len(elements) // 2, "-" + str(moves) + "a")
        elements.insert(len(elements) // 2 + 1, "-" + str(moves) + "a")
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue

    if elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        elements.pop(max(index1, index2))  # pop first the bigger index to pop the correct 2nd index
        elements.pop(min(index1, index2))
    else:
        print("Try again!")

    command = input()

if len(elements) == 0:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
