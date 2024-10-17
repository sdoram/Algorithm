input()
K = list(map(int, list(input())))
if sum([1 if k % 2 == 0 else -1 for k in K ]) == 0:
    print(-1)
elif sum([1 if k % 2 == 0 else -1 for k in K ]) > 0:
    print(0)
else :
    print(1)
    