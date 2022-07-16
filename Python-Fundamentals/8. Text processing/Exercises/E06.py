text = input()
# unique_letters = []
result = ""
for index, letter in enumerate(text):
    if index == len(text) - 1:
        result += letter
        continue
    if text[index] != text[index + 1]:
        result += letter

print(result)