nums = input()
beggars = int(input())

nums_list = list(map(int, nums.split(", ")))  # convert all elements to int

final_list = []

for i in range(beggars):
    middle_list = nums_list[i::beggars]
    final_list.append(sum(middle_list))

print(final_list)