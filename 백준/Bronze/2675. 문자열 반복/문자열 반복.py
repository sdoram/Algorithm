import sys
for _ in range(int(sys.stdin.readline())):
    R, S = sys.stdin.readline().split()
    P = ''
    for i in S:
        P += int(R)*i
    print(P)
    