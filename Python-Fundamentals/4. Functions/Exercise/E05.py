str_nums = input().split()
int_nums = [int(s) for s in str_nums]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, int_nums))
print(result)