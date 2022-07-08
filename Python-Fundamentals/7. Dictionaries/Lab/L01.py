data = input().split()
product_dict = {}

for i in range(0, len(data), 2):
    product_dict[data[i]] = int(data[i + 1])


print(product_dict)
