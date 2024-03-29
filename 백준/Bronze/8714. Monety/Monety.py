import sys
int(sys.stdin.readline())
COIN_TOSS = list(sys.stdin.readline().split())
print(min(COIN_TOSS.count('1'), COIN_TOSS.count('0')))