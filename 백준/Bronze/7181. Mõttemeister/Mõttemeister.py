N = input()
for _ in range(int(input())):
    A, B = 0, 0
    C = input()
    for i in range(4):
        if N[i] == C[i]:
            B += 1
    for c in set(list(C)):
        if c in N:
            A += min(C.count(c), N.count(c))
    print(A, B)