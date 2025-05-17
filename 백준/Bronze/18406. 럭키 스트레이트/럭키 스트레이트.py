N = input()
print('LUCKY' if sum(map(int, N[:len(N)//2])) == sum(map(int, N[len(N)//2:])) else 'READY')