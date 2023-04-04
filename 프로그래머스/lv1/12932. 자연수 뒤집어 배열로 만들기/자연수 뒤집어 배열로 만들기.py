def solution(n):
    # n은 자연수
    # pop(), slice()
    answer = []
    # n 형변환
    n = str(n)
    n = list(n)
    
    # for문의 범위를 설정하는데 성공했는데 헷갈린다.
    for i in range(1, (len(n)+1)):
        num = n.pop()
        answer.append(int(num))
    
    return answer