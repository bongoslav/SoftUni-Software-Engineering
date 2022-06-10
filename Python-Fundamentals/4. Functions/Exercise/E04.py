def sum_digits(number):
    odd_list = []
    even_list = []
    num_str = str(number)
    for digit in num_str:
        int_digit = int(digit)
        if int_digit % 2 == 0:
            even_list.append(int_digit)
        else:
            odd_list.append(int_digit)

    even_sum = sum(even_list)
    odd_sum = sum(odd_list)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


num = int(input())
print(sum_digits(num))