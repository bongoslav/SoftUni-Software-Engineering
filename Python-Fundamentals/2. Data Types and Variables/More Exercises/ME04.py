lines = int(input())

opening_brackets_count = 0
closing_brackets_count = 0
last_bracket = ""
is_balanced = True

for enters in range(lines):
    entry = input()
    if entry == "(":
        opening_brackets_count += 1
        if last_bracket == "(":
            is_balanced = False
    if entry == ")":
        closing_brackets_count += 1
        if last_bracket == ")":
            is_balanced = False
    last_bracket = entry

if opening_brackets_count == closing_brackets_count and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")