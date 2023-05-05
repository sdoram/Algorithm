def solution(A, B):
    right_count = -1
    for n in range(len(A)+1):
        if A[len(A)-n:]+A[:len(A)-n] == B:
            if right_count == -1:
                right_count = n
    return right_count