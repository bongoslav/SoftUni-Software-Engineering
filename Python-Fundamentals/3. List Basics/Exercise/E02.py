factor = int(input())
count = int(input())
nums_list = []

for multiplier in range(1, count + 1):
    nums_list.append(factor * multiplier)

print(nums_list)