names = input().split()

sorted_names = sorted(names, key=lambda name: (-len(name), name))  # if first criteria is already fulfilled
# (elements are of equal length), sort by second (alphabetically)

print(sorted_names)