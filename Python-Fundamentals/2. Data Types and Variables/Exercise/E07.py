number_of_lines = int(input())
total = 0
for line in range(number_of_lines):
    litres = int(input())
    if total + litres <= 255:
        total += litres
    else:
        print("Insufficient capacity!")

print(total)
    