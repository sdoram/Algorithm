N = int(input())
for i in range(1, N*5+1):
    if i > N*5 - N:
        print('@' * 5 * N)
    else:
        print('@' * N)