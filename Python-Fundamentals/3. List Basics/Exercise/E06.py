numbers_list = list(map(int, input().split()))  # convert to a list of ints
count_to_remove = int(input())

for count in range(count_to_remove):
    numbers_list.remove(min(numbers_list))

str_nums_list = [str(num) for num in numbers_list]
string_of_nums = ", ".join(str_nums_list)
print(string_of_nums)