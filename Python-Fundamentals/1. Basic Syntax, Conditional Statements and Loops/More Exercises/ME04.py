word = input().lower()

matches = ["water", "sand", "fish", "sun"]
word_count = 0
for match in matches:
    word_count += word.count(match)

print(word_count)