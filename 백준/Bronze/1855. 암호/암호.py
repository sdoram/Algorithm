K = int(input())
WORD = input()
NEW_WORD = []
for n in range(len(WORD) // K):
    if n % 2 == 0:
        NEW_WORD.append(WORD[n * K : (n + 1) * K])
    else:
        REVERSE_WORD = WORD[n * K : (n + 1) * K]
        NEW_WORD.append(REVERSE_WORD[::-1])
ANSWER = ""
for NW in range(len(NEW_WORD[0])):
    for N in NEW_WORD:
        ANSWER += N[NW]
print(ANSWER)