line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

has_won = False
winner = 0
# win if all of a column are equal
for index in range(0, len(line1) - 1):
    if line1[index] == line2[index] == line3[index]:
        has_won = True
        winner = line1[index]

# win if all of a row are equal
def all_same(items):
    return all(x == items[0] for x in items)


if all_same(line1):
    has_won = True
    winner = line1[0]
elif all_same(line2):
    has_won = True
    winner = line2[0]
elif all_same(line3):
    has_won = True
    winner = line3[0]

# win if either diagonal is equal
if line1[0] == line2[1] == line3[2] or line1[2] == line2[1] == line3[0]:
    has_won = True
    winner = line2[1]

if has_won and winner == 1:
    print("First player won")
elif has_won and winner == 2:
    print("Second player won")
else:
    print("Draw!")