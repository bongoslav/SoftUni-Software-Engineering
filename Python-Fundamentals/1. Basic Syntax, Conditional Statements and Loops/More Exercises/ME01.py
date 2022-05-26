number_given = int(input())

new_number = "".join(sorted(str(number_given), reverse=True))
print(new_number)