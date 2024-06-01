import sys
input = sys.stdin.readline

def sort_names(N):
    players = [input().rstrip()  for _ in range(N)]
    if players == sorted(players):
        return 'INCREASING'
    return 'DECREASING' if  players == sorted(players, reverse=True) else 'NEITHER'

print(sort_names(int(input())))