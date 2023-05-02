def solution(quiz):
    answer = []
    for q in quiz:
        q_split = q.split()
        sum_q = int(q_split[0])+int(q_split[2]) if q_split[1] == '+' else int(q_split[0])-int(q_split[2])
        answer.append("O") if sum_q == int(q_split[4]) else answer.append("X") 
    return answer