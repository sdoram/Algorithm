A = int(input())
B = input()
C = 0
print(A)
print(B)
for i, b in enumerate(B[::-1]):
    print(A*int(b))
    C += A*int(b+'0'*i)
print(C)