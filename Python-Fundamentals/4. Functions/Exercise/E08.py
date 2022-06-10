def is_palindrome(numbers: list):
    for number in numbers:
        if number == number[::-1]:
            print(True)
        else:
            print(False)


nums_list = list(input().split(", "))
is_palindrome(nums_list)