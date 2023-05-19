def solution(n):
    num_list = set(range(2,n+1))
    for num in sorted(num_list):
        for i in range(2, int((num - 1) ** 0.5 + 1) + 1):
            if num % i == 0 and num != i:
                num_list.remove(num)
                break
    return len(num_list)