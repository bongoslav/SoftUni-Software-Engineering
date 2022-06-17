strings1 = input().split(", ")
strings2 = input().split(", ")

result = []
for string1 in strings1:
    for string2 in strings2:
        if string1 in string2 and not strings1 in result:
            result.append(string1)
            break
print(result)
