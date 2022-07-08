stock = input().split()
searched_products = input().split()

available_products = {stock[i]: int(stock[i + 1]) for i in range(0, len(stock), 2)}

for product in searched_products:
    if product in available_products:
        print(f"We have {available_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
