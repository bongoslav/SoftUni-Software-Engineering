days = int(input())
players_count = int(input())
energy = float(input())
water_per_person = float(input())
total_water = water_per_person * players_count * days
food_per_person = float(input())
total_food = food_per_person * players_count * days

for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        break
    if day % 2 == 0:
        energy += 5 / 100 * energy
        total_water -= 30 / 100 * total_water
    if day % 3 == 0:
        total_food -= total_food / players_count
        energy += 10 / 100 * energy

if energy <= 0:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
