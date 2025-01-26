import sys

input = sys.stdin.readline

n = int(input())
gift_list = sorted([[int(input()), i] for i in range(1, n+1)])

for gift in gift_list:
    print(gift[1])