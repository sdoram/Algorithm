import math
def solution(n):
    # n은 사람 수 
    # return은 모든 사람이 피자를 한 조각 이상 먹는 피자의 수
    # n에 따라서 피자 수를 조절해야 함
    return math.ceil(n/7)