A = int(input())
B = [7 if i > 7 else i for i in map(int ,input().split())]
pa = len(B) * 2 + len(B) // 2
print(sum(B) - pa)