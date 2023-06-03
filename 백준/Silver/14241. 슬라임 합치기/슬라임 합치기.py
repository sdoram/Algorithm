N = int(input()) - 1
slime_list = list(map(int, input().split()))
SCORE = 0
for _ in range(N):
    SCORE += slime_list[0] * slime_list[1]
    slime_list[0] += slime_list.pop(1)
print(SCORE)