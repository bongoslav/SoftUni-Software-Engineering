# usernames = input().split(", ")
# for username in usernames:
#     is_valid = True
#     if not 3 <= len(username) <= 16:
#         is_valid = False
#         continue
#     for character in username:
#         if not (character.isalnum() or character == "-" or character == "_"):
#             is_valid = False
#             continue
#     if ' ' in username:
#         is_valid = False
#
#     if is_valid:
#         print(username)

######################################################################

# Solution with functions:
def valid_length(user):
    if 3 <= len(user) <= 16:
        return True
    return False


def valid_characters(user):
    for character in user:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(user):
    if ' ' in user:
        return False
    return True


usernames = input().split(", ")
for username in usernames:
    if valid_length(username) and valid_characters(username) and no_redundant_symbols(username):
        print(username)
