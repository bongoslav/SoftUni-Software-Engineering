def get_digits(data):
    return ''.join([str(ch) for ch in data if ch.isdigit()])


def get_letters(data):
    return ''.join([str(ch) for ch in data if ch.isalpha()])


def get_symbols(data):
    return ''.join([str(ch) for ch in data if not ch.isdigit() and not ch.isalpha()])


text = input()
print(get_digits(text))
print(get_letters(text))
print(get_symbols(text))
