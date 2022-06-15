todo_note = input()
temp_list = [""] * 11

while todo_note != "End":
    tokens = todo_note.split("-")
    importance = int(tokens[0])
    todo = tokens[1]
    temp_list[importance] = todo
    todo_note = input()

sorted_list = [value for value in temp_list if value != ""]
print(sorted_list)