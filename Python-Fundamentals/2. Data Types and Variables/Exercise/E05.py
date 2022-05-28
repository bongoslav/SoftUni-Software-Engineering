start_index = int(input())
end_index = int(input())
final_string = ""
for value in range(start_index, end_index + 1):
    final_string += chr(value) + " "
    # print(chr(value), end = " ")

print(final_string)