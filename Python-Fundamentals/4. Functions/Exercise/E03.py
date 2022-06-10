def characters_funct(start, end):
    char_list = [chr(element) for element in range(ord(start) + 1, ord(end))]
    return " ".join(char_list)


first_char = input()
second_char = input()
print(characters_funct(first_char, second_char))