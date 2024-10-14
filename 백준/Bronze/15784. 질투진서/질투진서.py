N, a, b = map(int, input().split())
seat = [list(map(int, input().split())) for _ in range(N)]
print('HAPPY' if seat[a-1][b-1] == max(seat[a-1]+[seat[i][b-1] for i in range(N)]) else 'ANGRY')