def solution(board):
    new_board = [[0]*len(board) for _ in board]
    for i1, b1 in enumerate(board):
        for i2, b2 in enumerate(b1):
            if b2 == 1:
                for n1 in range(i1-1, i1+2):
                    if len(board) > n1 >= 0:
                        for n2 in range(i2-1, i2+2):
                            if len(board) > n2 >= 0:
                                new_board[n1][n2] = 1
    return len(board)**2-sum([sum(n) for n in new_board])