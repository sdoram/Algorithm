import sys

input = sys.stdin.readline

score_list = sorted([input().split() for _ in range(int(input()))], key=lambda x: x[0])
score_list = sorted(score_list, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3])))
print('\n'.join([n[0] for n in score_list]))