num1 = int(input())
num2 = int(input())

print("Before:")
print(f"a = {num1}")
print(f"b = {num2}")

num_temp = num1
num1 = num2
num2 = num_temp

print("After:")
print(f"a = {num1}")
print(f"b = {num2}")