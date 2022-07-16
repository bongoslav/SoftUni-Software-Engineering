text = input()
for i, char in enumerate(text):
    if char == ":" and not text[i + 1].isdigit():
        print(text[i] + text[i + 1])

