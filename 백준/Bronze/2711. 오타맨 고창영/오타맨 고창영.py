import sys
for _  in range(int(sys.stdin.readline())):
    NUM, WORD = sys.stdin.readline().split()
    WORD = list(WORD)
    WORD.pop(int(NUM)-1)
    print(*WORD, sep='')