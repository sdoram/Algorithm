import sys
w = input()
A = sys.stdin.readlines()
print(sum([line.count(w) for line in A]))