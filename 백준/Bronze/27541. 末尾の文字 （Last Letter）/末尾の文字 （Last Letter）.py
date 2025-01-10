input()
word = input()
print(word[:-1] if word[-1] == 'G' else word + 'G')