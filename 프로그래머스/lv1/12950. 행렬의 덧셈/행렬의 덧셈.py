def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        zip_list = list(zip(arr1[i],arr2[i]))
        ans = []
        for n in zip_list:
            ans.append(sum(n))
        answer.append(ans)
    return answer