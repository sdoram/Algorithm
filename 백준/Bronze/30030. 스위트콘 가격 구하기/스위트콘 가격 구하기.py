B = int(input())
C = int(B / 1.1)
print(C if int(C * 1.1) == B else C+1)