for _ in range(int(input())):
    A, B, C, D = map(int, input().split())
    if B >= 11 and C >= 8 and D >= 12 and sum([B, C, D]) >= 55:
        print(f'{A} {sum([B, C, D])} PASS')
    else:
        print(f'{A} {sum([B, C, D])} FAIL')
