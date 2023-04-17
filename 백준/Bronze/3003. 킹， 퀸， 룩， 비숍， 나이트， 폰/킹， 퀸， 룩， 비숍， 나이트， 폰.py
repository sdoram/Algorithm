chess_list = [1, 1, 2, 2, 2, 8]
a = list(input().split())
answer = []
for idx, num in enumerate(chess_list):
    answer.append(str(num - int(a[idx])))
print(' '.join(answer))