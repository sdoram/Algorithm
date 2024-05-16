import sys
X = sys.stdin.readline().rstrip()
if X[:2] == '0x':
    print(int(X[2:], 16))
elif X[:1] == '0':
    print(int(X[1:], 8))
else:
    print(int(X))