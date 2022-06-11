def tribonacci(count):
    last_three_digits = [1]
    all_nums_list = [1]
    for number in range(count - 1):  # hardcoding
        sum_last_three = sum(last_three_digits)
        last_three_digits.append(sum_last_three)
        all_nums_list.append(sum_last_three)

        if len(last_three_digits) > 3:
            last_three_digits.pop(0)

    return " ".join(str(values) for values in all_nums_list)  # convert int to str to connect the elements


num = int(input())
print(tribonacci(num))