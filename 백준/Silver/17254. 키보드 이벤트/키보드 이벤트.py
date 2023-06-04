N, M = map(int, input().split())
print("".join([x[2]for x in sorted([input().split() for _ in range(M)], key=lambda x: [int(x[1]), int(x[0])])]))