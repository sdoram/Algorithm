def solution(numbers, direction):
    # direction에 따라서 numbers의 순서를 한 칸씩 이동
    # [1:] 사용하면 될까?
    # enumerate에 시작값 주면 될까?
    # left 마지막에 깔끔하게 [0]값을 줄 방법이 없나?
    answer = []
    if direction == 'left':
        for idx in range(-len(numbers)+1,1):
            answer.append(numbers[idx])
    else:
        for idx in range(-1,len(numbers[:-1])):
            answer.append(numbers[idx])
            
            
    return answer