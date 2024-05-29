import sys
input = sys.stdin.readline

A = list(input().split())
B = input().rstrip()

print(sum([1 if a[:len(B):] == B and a != B else 0 for a in A]))