input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B))
if len(A-B):
    print(*sorted(A-B))