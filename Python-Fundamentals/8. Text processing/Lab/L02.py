entry = input().split()

for word in entry:
    print(f'{word*len(word)}', end="")