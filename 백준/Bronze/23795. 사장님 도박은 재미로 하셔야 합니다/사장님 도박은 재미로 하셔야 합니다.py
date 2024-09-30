import sys

input = sys.stdin.readline

betting = 0
while True:
    n = int(input())
    if n == -1:
        break
    betting += n
print(betting)