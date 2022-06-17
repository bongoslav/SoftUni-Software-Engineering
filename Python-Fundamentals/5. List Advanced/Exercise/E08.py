message = input().split()

last_character = None
deciphered_sentence = []
for word in message:
    digits = ""
    letters = []
    character_count = 0
    for character in word:
        if character.isdigit():
            digits += character
        else:
            letters.append(character)
            character_count += 1
        current_character = character
        # find the end of the ascii number
        if current_character.isalpha() and last_character.isdigit():
            character_count += 1
        last_character = current_character
    letters[0], letters[-1] = letters[-1], letters[0]
    deciphered_word = chr(int(digits)) + "".join(letters)
    deciphered_sentence.append(deciphered_word)

print(" ".join(deciphered_sentence))