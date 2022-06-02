n = int(input())
word = input()

words_list = []
for i in range(n):
    words = input()
    words_list.append(words)
print(words_list)

for i in range(len(words_list) - 1, -1, -1):
    element = words_list[i]
    if word not in element:
        words_list.remove(element)
print(words_list)