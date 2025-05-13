w, h, d = map(int, input().split())
if min(w, h) <= d*2:
    print(0)
else:
    print((w-(d*2)) * (h-(d*2)))