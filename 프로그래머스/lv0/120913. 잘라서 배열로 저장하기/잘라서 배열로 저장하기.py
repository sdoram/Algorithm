def solution(my_str, n):
    answer = []
    instance = ''
    for i,s in enumerate(my_str,1):
        instance += s
        if i % n == 0 or len(my_str) == i:
            answer.append(instance)
            instance = ''
    return answer