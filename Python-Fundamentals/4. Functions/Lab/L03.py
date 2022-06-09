# # method 2:
# import operator
#
# def calculations(number_a, number_b, operation):
#     operations_dict = {"multiply": operator.mul, "divide": operator.truediv, "add": operator.add, "subtract":
#         operator.sub}
#     return int(operations_dict[operation](number_a, number_b))


# original method
def calculation_funct(given_command, num1, num2):
    result = None
    if given_command == "multiply":
        result = num1 * num2
    elif given_command == "divide":
        result = num1 // num2
    elif given_command == "add":
        result = num1 + num2
    elif given_command == "subtract":
        result = num1 - num2

    return result


command = input()
first_num = int(input())
second_num = int(input())

print(calculation_funct(command, first_num, second_num))