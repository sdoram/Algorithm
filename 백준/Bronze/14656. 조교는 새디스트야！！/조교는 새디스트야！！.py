input()
print(sum([1 for i, n in enumerate(map(int, input().split()), 1) if i != n]))