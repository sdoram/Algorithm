def find_dwarf():
    A = [int(input()) for _ in range(9)]
    for a in A:
        for i in range(9):
            if a != A[i] and sum(A) - (a + A[i]) == 100:
                A.pop(i)
                A.pop(A.index(a))
                return list(map(str, A))

print('\n'.join(find_dwarf()))