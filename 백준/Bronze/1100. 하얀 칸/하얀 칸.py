white = [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0]]
count = 0
chess_pieces = []

for _ in range(8):
    chess_piece = input()
    chess_pieces.append(chess_piece)
    
for idx, chess in enumerate(chess_pieces):
    for i, c in enumerate(chess):
        if c == 'F' and white[idx][i] == 0:
            count += 1
            
print(count)