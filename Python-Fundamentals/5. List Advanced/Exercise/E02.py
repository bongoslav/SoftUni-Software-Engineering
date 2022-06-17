version = input()

version = int(version.replace(".", ""))
version += 1
result = ".".join([digit for digit in str(version)])
print(result)
