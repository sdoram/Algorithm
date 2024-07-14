for _ in range(int(input())):
    input()
    N = sorted(input(), reverse=True)
    A, B = N[:-1:], int(N[-1])
    
    print(int(''.join(A))+B)