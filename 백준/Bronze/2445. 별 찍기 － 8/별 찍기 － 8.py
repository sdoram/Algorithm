N = int(input())
for n in range(1, N):
    print(('*'*n)+(' '*(2*(N-n)))+('*'*n))
print('*'*N*2)
for n in range(1, N)[::-1]:
    print(('*'*n)+(' '*(2*(N-n)))+('*'*n))