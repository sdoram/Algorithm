A, B = map(int, input().split())
print(min(abs(A-B), *[abs(B-int(input()))+1 for _ in range(int(input()))]))