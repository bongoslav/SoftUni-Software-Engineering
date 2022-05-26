# lists are mutable while strings are not
my_list = [1, 2, 3, "softuni"]
my_list[0] = "first element"

# tuple is immutable
my_tuple = (5, 6, "7")

# set is a collection of unique values
test = {"a", "c", "b", "c"}
# print(test)  # returns a, c, b

# dictionaries
person = {"name": "Ivan", "age": 32}
print(person["name"])