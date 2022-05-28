lost_fights = int(input())
helmet_price = float(input())
helmet_count = 0
sword_price = float(input())
sword_count = 0
shield_price = float(input())
shield_count = 0
armor_price = float(input())
armor_count = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        helmet_count += 1
    if fight % 3 == 0:
        sword_count += 1
        if fight % 2 == 0:
            shield_count += 1
            if shield_count % 2 == 0:
                armor_count += 1

expenses = helmet_count * helmet_price + sword_price * sword_count + shield_count * shield_price + armor_count * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")