N = int(input())
S = input()
T = input()
A, B = 0, 0

for i in range(N):
    if S[i] == 'R' and T[i] == 'S':
        A += 1
    if S[i] == 'P' and T[i] == 'R':
        A += 1
    if S[i] == 'S' and T[i] == 'P':
        A += 1
    if T[i] == 'R' and S[i] == 'S':
        B += 1
    if T[i] == 'P' and S[i] == 'R':
        B += 1
    if T[i] == 'S' and S[i] == 'P':
        B += 1
print(A, B)