budget = float(input())
flour_price = float(input())
eggs_price = 0.75*flour_price
milk_price = 1.25*flour_price / 4
loaves = 0
colored_eggs = 0

while True:
    old_budget = budget

    budget -= (flour_price + eggs_price + milk_price)
    # if loaves % 4 == 0:
    #     budget -= milk_price

    if budget < 0:
        budget = old_budget
        break
    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
