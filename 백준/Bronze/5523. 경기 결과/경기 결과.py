score = [0, 0]
for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        score[0] += 1
    elif B > A:
        score[1] += 1
print(*score)