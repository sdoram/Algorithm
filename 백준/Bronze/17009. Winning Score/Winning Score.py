A = [int(input()) for _ in range(3)]
B = [int(input()) for _ in range(3)]
A_SCORE = A[0] * 3 + A[1] * 2 + A[2]
B_SCORE = B[0] * 3 + B[1] * 2 + B[2]
print('T' if A_SCORE == B_SCORE else 'A' if A_SCORE > B_SCORE else 'B')