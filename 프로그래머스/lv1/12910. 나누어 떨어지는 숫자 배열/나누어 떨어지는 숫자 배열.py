def solution(arr, divisor):
    # arr을 for문으로 돌림
    # if arr % divisor == 0:
    # if문에 걸리는 수가 없으면 -1 return
    # sort() 사용
    answer = []
    
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if answer == []:
        answer.append(-1)
    answer.sort()
    
    return answer