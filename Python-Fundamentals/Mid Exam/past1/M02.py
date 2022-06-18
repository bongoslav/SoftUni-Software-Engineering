people_waiting = int(input())
state = list(map(int, input().split()))

for index, spot in enumerate(state):
    while state[index] < 4 and people_waiting > 0:
        state[index] += 1
        people_waiting -= 1

if min(state) < 4:
    print("The lift has empty spots!")
    print(" ".join([str(element) for element in state]))
elif min(state) == 4 and people_waiting == 0:
    print(" ".join([str(element) for element in state]))
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join([str(element) for element in state]))
