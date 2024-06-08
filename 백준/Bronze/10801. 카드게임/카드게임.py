A = list(map(int, input().split()))
B = list(map(int, input().split()))

score = sum([1 if a > B[i] else 0 if a == B[i] else -1 for i, a in enumerate(A)])
print('A' if score > 0 else 'D' if score == 0 else 'B')