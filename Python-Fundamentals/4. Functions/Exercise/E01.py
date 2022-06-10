def smallest_num(first, second, third):
    list_nums = [first, second, third]
    return min(list_nums)


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(smallest_num(first_num, second_num, third_num))