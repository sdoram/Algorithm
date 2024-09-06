def small_number():
    N = int(input())
    J = sorted(list(map(int, input().split())))
    S = sorted(list(map(int, input().split())))
    
    J_idx = 0
    S_idx = 0
    count = 0

    while J_idx < N and S_idx < N:
        if S[S_idx] > J[J_idx]:
            count += 1
            J_idx += 1
        S_idx += 1
        
    return 'YES' if int((N+1)//2) <= count else 'NO'

print(small_number())