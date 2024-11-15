N, M = map(int, input().split())
painting = [list(input()) for _ in range(N)]
for n in range(N):
    for i, p in enumerate(painting[n][::-1]):
        if "." != p:
            painting[n][i] = p
for p in painting:
    print("".join(p))