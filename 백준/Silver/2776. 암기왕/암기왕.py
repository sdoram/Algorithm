from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    N_word = {i: "1" for i in list(map(int, stdin.readline().split()))}
    M = int(stdin.readline())
    M_word = list(map(int, stdin.readline().split()))
    print("\n".join([N_word.get(m, "0") for m in M_word]))
