import math

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length_a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    length_b = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
    longest_line = max(length_a, length_b)
    if longest_line == length_a:
        closest_point = min(abs(x1) + abs(y1), abs(x2) + abs(y2))
        if closest_point == abs(x1) + abs(y1):
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    else:
        closest_point = min(abs(x3) + abs(y3), abs(x4) + abs(y4))
        if closest_point == abs(x3) + abs(y3):
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))