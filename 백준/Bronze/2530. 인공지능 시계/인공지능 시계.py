import sys
A, B, C = map(int,sys.stdin.readline().split())
D = int(sys.stdin.readline())
E = (A*60*60 + B*60 + C + D ) % 86400
print(E//60//60, E//60%60, E%60)