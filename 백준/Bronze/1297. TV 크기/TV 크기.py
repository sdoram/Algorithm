import sys, math
D, H, W = map(int, sys.stdin.readline().split())
B = (D**2 / (H**2 + W**2)) ** (1/2) 
print(math.trunc(B*H), math.trunc(B*W))