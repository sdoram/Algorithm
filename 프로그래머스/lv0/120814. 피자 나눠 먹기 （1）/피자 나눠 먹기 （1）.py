def solution(n):
    # while문의 조건식 not*7 pizza //n은 
    # 7*pizza //n이 0이 아닐때까지 반복한다. 
    # 이때 7*pizza //n은 pizza 판의 피자를 
    # n명이 나누어 먹을때 각 사람당 받게 되는 조각 수 
    # 따라서 7*pizza // n 이 0이 아닌 경우에 모든 사람이 
    # 최소한 한 조각 이상 먹을 수 있는 피자를 구할수 있다. 
    pizza = 1
    while 7 * pizza // n == 0:
        pizza += 1 
    return pizza