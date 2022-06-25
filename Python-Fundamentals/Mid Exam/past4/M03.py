homes = list(map(int, input().split("@")))

command = input()
cupid_position = 0
while command != "Love!":
    jump_length = int(command.split()[1])
    cupid_position += jump_length
    if cupid_position > len(homes) - 1:
        cupid_position = 0
    homes[cupid_position] -= 2
    if homes[cupid_position] < 0:
        homes[cupid_position] = 0
        print(f"Place {cupid_position} already had Valentine's day.")
    elif homes[cupid_position] == 0:
        print(f"Place {cupid_position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {cupid_position}.")
if max(homes) == 0:  # if each house is 0
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(homes) - homes.count(0)} places.")