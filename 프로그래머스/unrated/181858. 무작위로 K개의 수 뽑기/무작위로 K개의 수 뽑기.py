def solution(arr, k):
    answer = []
    count = 0
    while count != k:
        for i in range(len(arr)):
            if arr[i] not in answer:
                count += 1
                answer.append(arr[i])
            if count == k:
                return answer
        return answer + [-1 for _ in range(k - len(answer))]