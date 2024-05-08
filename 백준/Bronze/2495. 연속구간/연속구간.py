import sys
for _ in range(3):
    NUM = sys.stdin.readline().rstrip()
    a, b, c = '', 1, [1]
    for n in NUM:
        if a != n:
            a, b = n, 1
            c.append(b)
        else:
            b += 1
            c.append(b)
    print(max(c))