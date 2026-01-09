A, B = map(int, input().split(':'))
C, D = map(int, input().split(':'))
print('YES' if C*60+D > A*60+B else 'NO')