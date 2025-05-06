for _ in range(int(input())):
    N = int(input())
    print(sum([i for i in range(1, N+1)]), sum([i for i in range(1, N*2+1, 2)]), sum([i for i in range(2, (N+1)*2, 2)]))