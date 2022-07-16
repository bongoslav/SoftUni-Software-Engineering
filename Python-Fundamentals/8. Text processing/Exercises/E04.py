text = input()
result = ""
for letter in text:
    letter = chr(ord(letter) + 3)
    result += letter

print(result)