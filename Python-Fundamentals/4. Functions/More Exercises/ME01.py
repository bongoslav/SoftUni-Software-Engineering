def data_types(type_of_data, data):
    if type_of_data == "int":
        return int(data) * 2
    elif type_of_data == "real":
        return f"{float(data) * 1.5:.2f}"
    elif type_of_data == "string":
        return f"${data}$"


data_type = input()
input_string = input()
print(data_types(data_type, input_string))