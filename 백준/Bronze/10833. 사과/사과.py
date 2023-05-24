ANSWER = 0
for _ in range(int(input())):
    A, N = map(int, input().split())
    ANSWER += N % A
print(ANSWER)
