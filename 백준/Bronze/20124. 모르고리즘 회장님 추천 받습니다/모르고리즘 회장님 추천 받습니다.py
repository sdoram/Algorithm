import sys

input = sys.stdin.readline

candidate_dict = {}
for name, score in sorted([input().split() for _ in range(int(input()))]):
    if int(score) not in candidate_dict:
        candidate_dict[int(score)] = name
print(candidate_dict[max(candidate_dict)])