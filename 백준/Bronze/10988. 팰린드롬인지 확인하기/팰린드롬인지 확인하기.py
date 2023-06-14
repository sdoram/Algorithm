def palindrome(word):
    return 1 if word == word[::-1] else 0


print(palindrome(input()))
