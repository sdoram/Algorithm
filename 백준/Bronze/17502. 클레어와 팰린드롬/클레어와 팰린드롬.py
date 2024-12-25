N = int(input())
word = input()
new_word = str()
for i, w in enumerate(word, 1):
    if w == '?' and word[N-i] == '?':
        new_word += 'a'
    elif w == '?':
        new_word += word[N-i]
    else:
        new_word += w
print(new_word)