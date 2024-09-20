for _ in range(int(input())):
    A = input()
    B = input()
    print(f'Hamming distance is {sum([1 if A[i] != B[i] else 0 for i in range(len(A))])}.')