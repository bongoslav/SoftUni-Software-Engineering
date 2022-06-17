def positive(nums):
    return [num for num in nums if int(num) >= 0]
def negative(nums):
    return [num for num in nums if int(num) < 0]
def even(nums):
    return [num for num in nums if int(num) % 2 == 0]
def odd(nums):
    return [num for num in nums if int(num) % 2 != 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")