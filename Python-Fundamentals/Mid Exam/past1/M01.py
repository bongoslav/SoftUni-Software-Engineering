command = input()
total_no_taxes = 0
total_with_taxes = 0
taxes = 0
is_valid = True
while True:
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_no_taxes += price
    taxes += price * 0.2
    command = input()

total_with_taxes = (total_no_taxes + taxes)
if total_no_taxes == 0:
    print("Invalid order!")
    is_valid = False
elif command == "special":
    total_with_taxes *= 0.9

if is_valid:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_no_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_with_taxes:.2f}$")
