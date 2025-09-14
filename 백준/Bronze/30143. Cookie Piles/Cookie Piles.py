for _ in range(int(input())):
    N, A, D = map(int, input().split())
    print(sum([A+i*D for i in range(N)]))