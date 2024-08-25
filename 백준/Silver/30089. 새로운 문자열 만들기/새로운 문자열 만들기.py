import sys

input = sys.stdin.readline

def new_word():
    X = input().rstrip()
    words = []
    if len(X) % 2 == 0 and X[len(X)//2:] == X[len(X)//2-1::-1]:
        return X
    elif len(X) % 2 != 0 and X[len(X)//2:] ==  X[len(X)//2::-1]:
        return X
    for i in range(len(X)):
        word = X + X[i::-1]
        if len(word) % 2 == 0 and word[len(word)//2:] == word[len(word)//2-1::-1]:
            words.append(word)
        elif len(word) % 2 != 0 and word[len(word)//2:] ==  word[len(word)//2::-1]:
            words.append(word)
    return sorted(words, key=len)[0]

for _ in range(int(input())):
    print(new_word())