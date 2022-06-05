numbers = input()
some_string = list(input())
indexes_list = numbers.split()
word = []
for number_index in indexes_list:
    for message_index, message_char in enumerate(some_string):
        digit_sum = 0
        for digit in number_index:
            digit_sum += int(digit)

        if digit_sum > len(some_string):
            digit_sum -= len(some_string)

        if message_index == digit_sum:
            word_char = some_string.pop(message_index)  # remove and return the char
            word.append(word_char)
            break
print("".join(word))