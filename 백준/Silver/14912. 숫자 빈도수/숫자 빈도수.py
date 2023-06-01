n, d = input().split()
print(sum([True for i in range(1, int(n) + 1) for j in str(i) if d in j]))