N, X = map(int, input().split())
bus = []
for _ in range(N):
    S, T = map(int, input().split())
    if X >= S+T:
        bus.append([S,T])
print(-1 if len(bus) == 0 else bus[bus.index(max(bus))][0])