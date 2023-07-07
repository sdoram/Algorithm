from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    N_word = {i: True for i in list(map(int, stdin.readline().split()))}
    M = int(stdin.readline())
    M_word = list(map(int, stdin.readline().split()))
    print("\n".join([str(int(N_word.get(m, False))) for m in M_word]))