A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

print(min(A*P, B + max(P-C, 0) * D))