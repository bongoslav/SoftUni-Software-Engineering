energy = int(input())

command = input()
counter = 0
distance = 0
while True:
    if command == "End of battle":
        print(f"Won battles: {counter}. Energy left: {energy}")
        break
    distance = int(command)
    if energy >= distance:
        energy -= distance
        counter += 1
        if counter % 3 == 0:
            energy += counter
        command = input()
    else:
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        break