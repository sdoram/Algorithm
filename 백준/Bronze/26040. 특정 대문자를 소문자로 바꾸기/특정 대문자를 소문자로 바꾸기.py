word = input()
replace_word_list = list(input().split())
for replace_word in replace_word_list:
    word = word.replace(replace_word, replace_word.lower())
print(word)