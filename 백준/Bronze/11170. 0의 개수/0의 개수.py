for _ in range(int(input())):
    N, M = map(int, input().split())
    print(sum([str(i).count('0') for i in range(N, M+1)]))