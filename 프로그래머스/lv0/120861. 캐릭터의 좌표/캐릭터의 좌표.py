def solution(keyinput, board):
    key_dict = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    max_board = board[0]//2, board[1]//2
    answer = [0,0]
    for key in keyinput:
        if abs(answer[0]+key_dict[key][0]) <= max_board[0] :
            answer[0] += key_dict[key][0]
        if  abs(answer[1]+key_dict[key][1]) <= max_board[1]:
            answer[1] += key_dict[key][1]
    return answer