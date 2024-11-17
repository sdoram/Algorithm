N = list(input() for _ in range(int(input())))
M = []
for i in range(len(N)):
    m = ''
    for j in range(len(N)):
        m += N[j][i]
    M.append(m)
print('YES' if N == M else 'NO')