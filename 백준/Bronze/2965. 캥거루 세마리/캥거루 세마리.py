import sys
A, B, C = map(int,sys.stdin.readline().split())
print(max(C-B, B-A)-1)