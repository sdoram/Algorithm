N = int(input())
for n in range(1, N)[::-1]:
    n = ' '*(2*n)
    print(f"{n:*^{N*2}}")
print('*'*N*2)
for n in range(1, N):
    n = ' '*(2*n)
    print(f"{n:*^{N*2}}")