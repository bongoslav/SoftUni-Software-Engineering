vowels = ["a", "o", "u", "e", "i"]

text = input()

new_text = "".join([letter for letter in text if letter not in vowels])
print(new_text)