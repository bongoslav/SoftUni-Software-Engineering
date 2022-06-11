def perfect_number(number):
    sum_numbers = 0
    for a_number in range(1, number + 1):
        if number % a_number == 0:
            sum_numbers += a_number

    if sum_numbers == 2 * number:
        return "We have a perfect number!"
    return "It's not so perfect."


num = int(input())
print(perfect_number(num))