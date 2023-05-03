def solution(l, r):
    answer = []
    for num in range(l,r+1):
        five_zero = str(num).count('0')+str(num).count('5')
        if len(str(num)) == five_zero:
            answer.append(num)
    if answer == []:
        answer.append(-1)
    return answer