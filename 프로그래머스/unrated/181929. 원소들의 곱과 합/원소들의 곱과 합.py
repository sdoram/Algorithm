def solution(num_list):
    # 0 원소들의 곱 > 원소들의 합의 제곱 1 
    answer = 0
    nums = 1
    for num in num_list:
        nums *= num
    return 0 if nums > pow(sum(num_list),2) else 1