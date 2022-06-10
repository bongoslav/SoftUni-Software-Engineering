def sum_numbers(first, second):
    return first + second

def subtract(first, second):
    return first - second

def add_and_subtract(first, second, third):
    sum_of_nums = sum_numbers(first, second)
    result = subtract(sum_of_nums, third)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))