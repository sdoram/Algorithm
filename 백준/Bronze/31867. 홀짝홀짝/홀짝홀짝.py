input()
K = list(map(int, list(input())))
if sum([1 for k in K if k % 2 == 0]) > sum([1 for k in K if k % 2 != 0]):
    print(0)
elif sum([1 for k in K if k % 2 == 0]) < sum([1 for k in K if k % 2 != 0]):
    print(1)
else:
    print(-1)