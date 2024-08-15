N, T = map(int, input().split())
bus_list = []
for _ in range(N):
    S, I, C = map(int, input().split())
    for c in range(C):
        if S+I*c >= T:
            bus_list.append(S+I*c-T)
            break
print(min(bus_list) if len(bus_list) != 0 else -1)