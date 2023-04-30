import sys
T = int(sys.stdin.readline())
for _ in range(T):
    num = list(sys.stdin.readline().split())
    answer = 0
    for n in num:
        try:
            answer += float(n)
        except ValueError:
            if n == '@':
                answer *= 3
            elif n == '%':
                answer += 5
            else:
                answer -= 7
    print("{:.2f}".format(answer))