N = input()
a = True
for i, n in enumerate(N, 1):
    if i != int(n):
        a = False
print(len(N) if a else -1)