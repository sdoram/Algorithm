def solution(n):
    # n 은 정수 
    if n % 2 == 0:
        answer = sum([num**2 for num in range(n+1) if num % 2 == 0])
    else:
        answer = sum([num for num in range(n+1) if num % 2 != 0])
    return answer