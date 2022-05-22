word_given = input()

capital_letters_index = []
for index, char in enumerate(word_given):
    if char.isupper():
        capital_letters_index.append(index)

print(capital_letters_index)