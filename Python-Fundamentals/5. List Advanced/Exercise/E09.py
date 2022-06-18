strings_list = input().split()
command = input()

result = ""
while command != "3:1":
    command = command.split()
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        # !!! check for indexes !!!
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings_list):
            end_index = len(strings_list) - 1
        strings_list[start_index:end_index + 1] = ["".join(strings_list[start_index:end_index + 1])]
    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        current_string = strings_list[index]
        result_current_string = []
        length_of_partition = len(current_string) // partitions
        for i in range(0, len(current_string), length_of_partition):
            part = current_string[i:i + length_of_partition]
            if i < partitions * length_of_partition:
                result_current_string.append(part)
            else:
                result_current_string[-1] += part
        strings_list[index:index + 1] = result_current_string

    command = input()

print(" ".join(strings_list))