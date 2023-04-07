def solution(n, numlist):
    # n의 배수만 골라서 return해라
    # numlist에서 % n을 했을 때 0인 것만 추출
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer