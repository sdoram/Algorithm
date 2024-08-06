N = int(input())
num_list = []
puzzle = [list(map(int, input().split())) for _ in range(N)]
# 가로줄
for p in puzzle:
    num_list.append(sum(p))

# 세로줄
for i in range(N):
    num_list.append(sum([puzzle[i][j] for j in range(N)]))
        
# 대각선
num_list.append(sum([puzzle[i][i] for i in range(N)]))
num_list.append(sum([puzzle[i][N-i-1] for i in range(N)]))

# 비어있는 수가 0이므로 바꿔야 하는 부분이 포함된 수가 작아야 정상
print(max(num_list)-min(num_list) if len(set(num_list)) == 2 and 
      num_list.count(max(num_list)) >= num_list.count(min(num_list)) else -1)