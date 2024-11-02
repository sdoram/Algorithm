input()
BSA = input()
B = BSA.count('B')
S = BSA.count('S')
A = BSA.count('A')
max_interest = ''

if B == S == A:
    print('SCU')
else:
    if B == max(B, S, A):
        max_interest += 'B'
    if S == max(B, S, A):
        max_interest += 'S'
    if A == max(B, S, A):
        max_interest += 'A'
    print(max_interest)