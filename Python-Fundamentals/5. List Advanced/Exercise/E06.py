total_electrons = int(input())
shells = []
level = 1
while True:
    shell_limit = 2 * level ** 2
    electrons_to_level = 0
    while electrons_to_level < shell_limit and total_electrons > 0:
        electrons_to_level += 1
        total_electrons -= 1

    shells.append(electrons_to_level)
    if total_electrons == 0:
        break
    level += 1


print(shells)