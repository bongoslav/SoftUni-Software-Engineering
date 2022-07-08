command = input()
products_dict = {}
while command != "statistics":
    entry = command.split(": ")
    product = entry[0]
    quantity = int(entry[1])
    if product not in products_dict:
        products_dict[product] = 0
    products_dict[product] += quantity

    command = input()

print("Products in stock:")
for key, value in products_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {sum(products_dict.values())}")
