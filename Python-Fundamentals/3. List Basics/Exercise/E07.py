gifts_list = input().split()
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        command, gift_in_interest = command.split()
        for index in range(len(gifts_list)):
            if gifts_list[index] == gift_in_interest:
                gifts_list[index] = "None"
    elif "Required" in command:
        command, gift_in_interest, index = command.split()
        given_index = int(index)
        if 0 < given_index < len(gifts_list):
            gifts_list[given_index] = gift_in_interest
    elif "JustInCase" in command:
        command, gift_in_interest = command.split()
        gifts_list[-1] = gift_in_interest
    command = input()

for index in range(len(gifts_list)):
    if "None" in gifts_list:
        gifts_list.remove("None")

print(" ".join(gifts_list))