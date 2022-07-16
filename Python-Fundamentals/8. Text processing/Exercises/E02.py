string1, string2 = input().split()

total = 0
shortest = min(len(string1), len(string2))
longest = max(len(string1), len(string2))

for i in range(shortest):
    total += ord(string1[i]) * ord(string2[i])

if shortest != longest:
    if len(string1) > len(string2):
        for i in range(shortest, longest):
            total += ord(string1[i])
    else:
        for i in range(shortest, longest):
            total += ord(string2[i])

print(total)