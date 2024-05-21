import sys, math
input = sys.stdin.readline

def packaging(T):
    ANSWER = []
    for _ in range(T):
        J, N = map(int, input().split())
        # math.prod() <= python 내장 곱하기 함수
        boxes = sorted([math.prod(map(int, input().split())) for _ in range(N)], reverse=True)
        
        for i, box in enumerate(boxes, start=1):
            J -= box
            if J <= 0:
                ANSWER.append(i)
                break
    return ANSWER

print(*packaging(int(input())), sep='\n')