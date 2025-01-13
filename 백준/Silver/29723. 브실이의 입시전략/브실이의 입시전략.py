import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
subject_dict = {}

for _ in range(N):
    S, P = input().split()
    subject_dict[S] = int(P)
    
open_subject = [input().rstrip() for _ in range(K)]
open_subject_score = sum([subject_dict[open_sub] for open_sub in open_subject])
not_open_subject = [value for key, value in subject_dict.items() if key not in open_subject]
min_score = sum(sorted(not_open_subject)[:M-K]) + open_subject_score
max_score = sum(sorted(not_open_subject, reverse=True)[:M-K]) + open_subject_score
print(min_score, max_score)