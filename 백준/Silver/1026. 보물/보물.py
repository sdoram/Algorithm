N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
new_b = []
answer = 0
for i, num in enumerate(B):
    new_b.append([num, i])
A.sort(reverse=True)
new_b.sort()
for n in range(N):
    answer += A[n] * new_b[n][0]
print(answer)