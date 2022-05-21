string1 = input()
string2 = input()
last_string = string1

for symbol in range(len(string1)):
    left_part = string2[:symbol + 1]
    right_part = string1[symbol + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string
    