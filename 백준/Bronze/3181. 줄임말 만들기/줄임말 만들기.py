import sys
WORD_LIST = sys.stdin.readline().split()
TEST_WORD = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
ABBREVIATION = [WORD_LIST[0][0].upper()]
for w in WORD_LIST[1::]:
    if w not in TEST_WORD:
        ABBREVIATION.append(w[0].upper())
print(*ABBREVIATION, sep='')