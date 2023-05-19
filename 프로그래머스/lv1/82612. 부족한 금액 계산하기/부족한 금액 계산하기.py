def solution(price, money, count):
    total = sum([price * i for i in range(1,count+1)])-money
    return total if total > 0 else 0