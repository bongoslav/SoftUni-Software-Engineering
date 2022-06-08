people_list = input().split(' ')
kill_count = int(input())
executed_list = []
counter = 0

index = 0
while len(people_list) > 0:
    counter += 1

    if counter % kill_count == 0:
        executed_list.append(people_list.pop(index))
    else:
        index += 1

    if index >= len(people_list):
        index = 0

print(str(executed_list).replace(' ', '').replace('\'', ''))