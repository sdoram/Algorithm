for t in range(int(input())):
    A = list(input().split())
    ANSWER = float(A[0])
    for i in A:
        if i == '@':
            ANSWER *= 3
        elif i == '%':
            ANSWER += 5
        elif i == '#':
            ANSWER -= 7
    print(f'{ANSWER:.2f}')