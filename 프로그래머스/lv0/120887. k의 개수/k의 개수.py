def solution(i, j, k):
    # i~j까지 k의 등장 횟수
    # 2중 for문 i~j 1번 각 숫자가 k가 있는지 1번
    answer = 0
    for num in range(i,j+1):
        for n in str(num):
            if int(n) == k:
                answer +=1
    return answer