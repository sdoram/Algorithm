from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    N_word = {i: True for i in list(map(int, stdin.readline().split()))}
    M = int(stdin.readline())
    M_word = list(map(int, stdin.readline().split()))
    for m in M_word:
        print(int(N_word.get(m, False)))