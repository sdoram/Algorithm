k = int(input())
input()
n = list(map(int, input().split()))
print('YES' if sum(n) - min(n) >= k else 'NO')