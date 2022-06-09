# numbers = list(map(float, input().split()))
#
# result = [abs(num) for num in numbers]
#
# print(result)

# ----------------------------------------- #

def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result


numbers = list(map(float, input().split()))

print(abs_numbers(numbers))
