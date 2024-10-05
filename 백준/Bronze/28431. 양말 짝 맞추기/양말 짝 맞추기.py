socks = {i:0 for i in range(10)}
for _ in range(5):
    n = int(input())
    if socks[n] == 0:
        socks[n] += 1
    else:
        socks[n] -= 1
print([key for key, value in socks.items() if value == 1][0])