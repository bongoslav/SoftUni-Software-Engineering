def calculate_factorial(num):
    factorial = 1
    for number in range(num, 1, -1):
        factorial *= number
    return factorial


number_a = int(input())
number_b = int(input())
factorial_a = calculate_factorial(number_a)
factorial_b = calculate_factorial(number_b)
print(f"{factorial_a / factorial_b:.2f}")