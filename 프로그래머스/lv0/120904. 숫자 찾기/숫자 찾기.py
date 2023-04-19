# 혼자 풀었을 때 코드 리팩토링
def solution(num, k):
    answer = -1
    num = str(num)
    # 반복문으로 n과 k가 일치하는 순간을 찾음
    for i, n in enumerate(num, 1):
        if int(n) == k:
            answer = i
            break

    return answer