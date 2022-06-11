import math


def closest_to_center(x1, y1, x2, y2):
    distance_a = abs(x1) + abs(y1)
    distance_b = abs(x2) + abs(y2)
    closest_point = min(distance_a, distance_b)
    if closest_point == distance_a:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    return f"({math.floor(x2)}, {math.floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_to_center(x1, y1, x2, y2))