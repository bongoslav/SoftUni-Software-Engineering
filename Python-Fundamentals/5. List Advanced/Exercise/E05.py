rooms = int(input())
free_chairs = 0
chairs = 0
visitors = 0
are_enough = True
for room in range(1, rooms + 1):
    info = input()
    chairs = len(info.split()[0])
    visitors = int(info.split()[1])
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        are_enough = False
    elif chairs > visitors:
        free_chairs += chairs - visitors

if are_enough:
    print(f"Game On, {free_chairs} free chairs left")
