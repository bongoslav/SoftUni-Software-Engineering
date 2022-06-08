items_list = input().split("|")
budget = float(input())
old_prices = []
for item_with_price in items_list:
    item = item_with_price.split("->")[0]
    price = float(item_with_price.split("->")[1])
    if (item == "Clothes" and price <= 50) or \
            (item == "Shoes" and price <= 35) or \
            (item == "Accessories" and price <= 20.50):
        if budget >= price:
            budget -= price
            old_prices.append(price)

new_prices = [old_price * 1.4 for old_price in old_prices]
profit = sum(new_prices) - sum(old_prices)

for price in new_prices:
    print(f"{price:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")

if sum(new_prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
