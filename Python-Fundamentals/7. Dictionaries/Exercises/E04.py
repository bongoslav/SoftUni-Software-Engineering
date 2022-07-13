people_dict = {}
entry = input()
while len(entry) > 1:
    name, number = entry.split("-")
    if name not in people_dict:
        people_dict[name] = ""
    people_dict[name] = number

    entry = input()

search_count = int(entry)
for count in range(search_count):
    name = input()
    if name in people_dict:
        print(f"{name} -> {people_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")