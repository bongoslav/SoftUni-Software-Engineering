number_of_chars = int(input())

total = 0
for _ in range(number_of_chars):
    char = input()
    char_value = ord(char)
    total += char_value

print(f"The sum equals: {total}")