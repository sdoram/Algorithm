word = input().split('+')
if len(word) == 2 and word[0] == word[1]:
    if sum([int(w) for w in word if w.isdigit()]) != 0:
        print('CUTE')
    else:
        print('No Money')
else:
    print('No Money')