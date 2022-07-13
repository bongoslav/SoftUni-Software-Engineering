products_dict = {}
command = input()
while command != "buy":
    product_info = command.split()
    product = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])
    info = {"price": price, "quantity": quantity}
    if product not in products_dict:
        products_dict[product] = info
    else:
        products_dict[product]["quantity"] += quantity
        products_dict[product]["price"] = price

    command = input()

for item, info in products_dict.items():
    print(f"{item} -> {info['price'] * info['quantity']:.2f}")