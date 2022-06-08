events = input().split("|")
energy = 100
coins = 100
events_count = 0
for event in events:
    event_ingredient_name = event.split("-")[0]
    number = int(event.split("-")[1])
    if event_ingredient_name == "rest":
        old_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        print(f"You gained {energy - old_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_ingredient_name == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:  # we have an ingredient with a price number
        if coins >= number:
            coins -= number
            print(f"You bought {event_ingredient_name}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient_name}.")
            break
    events_count += 1

if events_count == len(events):
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")