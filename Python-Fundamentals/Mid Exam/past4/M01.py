food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
day = 0
while True:
    day += 1
    food -= 300
    if day % 2 == 0:
        hay -= 5/100 * food  # 5% of the food
    if day % 3 == 0:
        cover -= 1/3 * weight

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break

    if day == 30:
        print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, "
              f"Cover: {cover / 1000:.2f}.")
        break