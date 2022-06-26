cards = input().split(", ")
num_commands = int(input())

for count in range(num_commands):
    command = input()
    tokens = command.split(", ")
    action = tokens[0]
    if action == "Add":
        card_name = tokens[1]
        if card_name not in cards:
            cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif action == "Remove":
        card_name = tokens[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(tokens[1])
        if 0 <= index < len(cards):
            cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action == "Insert":
        index = int(tokens[1])
        card_name = tokens[2]
        if index < 0 or index >= len(cards):
            print("Index out of range")
        elif card_name in cards:
            print("Card is already added")
        else:
            cards.insert(index, card_name)
            print("Card successfully added")

print(", ".join(cards))