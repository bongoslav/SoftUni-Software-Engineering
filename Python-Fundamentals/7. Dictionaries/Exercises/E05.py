useful_items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()
while True:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in useful_items:
            useful_items[key] = 0
        useful_items[key] += value
        if useful_items['shards'] >= 250:
            print("Shadowmourne obtained!")
            useful_items['shards'] -= 250
            obtained = True
        elif useful_items['fragments'] >= 250:
            print("Valanyr obtained!")
            useful_items['fragments'] -= 250
            obtained = True
        elif useful_items['motes'] >= 250:
            print("Dragonwrath obtained!")
            useful_items['motes'] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

    command = input().split()

for material, quantity in useful_items.items():
    print(f"{material}: {quantity}")
