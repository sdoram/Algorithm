from sys import stdin

count = 0
while True:
    count += 1
    n = int(stdin.readline().strip())
    if n == 0:
        break
    n1 = 3 * n
    n2 = n1 // 2 if n1 % 2 == 0 else (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    # n = 2 * n4 if n1 % 2 == 0 else 2 * n4 + 1
    print(f"{count}. {'even' if n1 % 2 == 0 else 'odd'} {n4}")
