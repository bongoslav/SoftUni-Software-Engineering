given_string = input()

while given_string != "End":
    new_string = ""
    if given_string != "SoftUni":
        for char in given_string:
            new_string += 2*char
        print(new_string)
       
    given_string = input()
