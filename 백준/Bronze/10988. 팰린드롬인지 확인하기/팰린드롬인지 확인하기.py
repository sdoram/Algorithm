def palindrome(word):
    for idx1, w in enumerate(word):
        for idx2, reverse_w in enumerate(word[::-1]):
            if idx1 == idx2:
                if w != reverse_w:
                    return 0
    return 1


print(palindrome(input()))