words = input().split()
palindrome = input()
palindromes_list = []
for word in words:
    # if word == word[::-1]: - much slower
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindromes_list.append(word)



print(palindromes_list)
count = words.count(palindrome)
print(f"Found palindrome {count} times")