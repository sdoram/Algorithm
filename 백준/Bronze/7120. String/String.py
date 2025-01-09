word = input()
current_w = word[0]
new_word = word[0]
for w in word:
    if current_w !=  w:
        new_word += w
        current_w = w
print(new_word)