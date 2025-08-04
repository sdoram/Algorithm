N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

print(''.join([chr(i+65) for i, score in enumerate(score_list) if score == max_score]))