import string

def anagram(first, second):
    alphabet = list(string.ascii_lowercase)
    return sum([abs(first.count(a) - second.count(a)) for a in alphabet])

print(anagram(input(), input()))
