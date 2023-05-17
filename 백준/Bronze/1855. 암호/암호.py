K = int(input())
WORD = input()
NEW_WORD = []
for n in range(len(WORD) // K):
    if n % 2 == 0:
        NEW_WORD.append(WORD[n * K : (n + 1) * K])
    else:
        REVERSE_WORD = WORD[n * K : (n + 1) * K]
        NEW_WORD.append(REVERSE_WORD[::-1])
WORD_LIST = []
for nw in NEW_WORD:
    word = []
    for w in nw:
        word.append(w)
    WORD_LIST.append(word)
WORD_LIST = list(zip(*WORD_LIST))
FIRST_WORD = ""
for word in WORD_LIST:
    FIRST_WORD += "".join(word)
print(FIRST_WORD)