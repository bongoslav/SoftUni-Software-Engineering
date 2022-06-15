wagons = int(input())
train = [0 for zero in range(wagons)]
command = input()

while command != "End":
    explode = command.split()
    current = explode[0]
    if current == "add":
        people = int(explode[1])
        train[-1] += people
    elif current == "insert":
        index = int(explode[1])
        people = int(explode[2])
        train[index] += people
    elif current == "leave":
        index = int(explode[1])
        people = int(explode[2])
        train[index] -= people

    command = input()

print(train)