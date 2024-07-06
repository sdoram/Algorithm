for i in range(1, int(input())+1):
    N = sorted(list(map(int, input().split()))[1:])
    print(f'Class {i}')
    print(f'Max {max(N)}, Min {min(N)}, Largest gap {max([abs(N[i-1]-n) for i, n in enumerate(N) if i != 0])}')