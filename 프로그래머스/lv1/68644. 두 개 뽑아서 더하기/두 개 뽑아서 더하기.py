def solution(numbers):
    answer = []
    for _ in range(len(numbers)):
        pop_num = numbers.pop()
        for num in numbers:
            answer.append(num+pop_num)
    return sorted(set(answer))