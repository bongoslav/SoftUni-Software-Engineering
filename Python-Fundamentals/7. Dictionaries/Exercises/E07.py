commands_num = int(input())
people_dict = {}
for count in range(commands_num):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        plate_num = command[2]
        if username not in people_dict:
            people_dict[username] = plate_num
            print(f"{username} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")

    if command[0] == "unregister":
        if username not in people_dict:
            print(f"ERROR: user {username} not found")
        else:
            del people_dict[username]
            print(f"{username} unregistered successfully")

for person, plate in people_dict.items():
    print(f"{person} => {plate}")