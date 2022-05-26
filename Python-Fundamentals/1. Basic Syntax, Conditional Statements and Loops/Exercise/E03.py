n = int(input())

custom_message = ""
for _ in range(0, n):
    number = int(input())
    if number == 88:
        custom_message = "Hello"
    elif number == 86:
        custom_message = "How are you?"
    elif number < 88:
        custom_message = "GREAT!"
    else:
        custom_message = "Bye."
    print(custom_message)