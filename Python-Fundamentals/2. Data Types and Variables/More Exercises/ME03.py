key = int(input())
lines = int(input())
message_list = []

for line in range(lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    message_list.append(new_letter)

message = "".join(message_list)
print(message)