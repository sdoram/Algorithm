def solution(n):
    # n을 각각 분리해서 내림차순으로 새롭게 정렬하기
    # list로 만들고, sort를 쓰고 pop()으로 꺼내기
    answer = ''
    n = str(n)
    n = list(n)
    n.sort()
    
    for i in range(1,len(n)+1):
        answer += n.pop()
    return int(answer)