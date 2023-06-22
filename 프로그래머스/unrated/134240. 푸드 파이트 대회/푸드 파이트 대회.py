def solution(food):
    answer = [str(i)*(f//2) for i, f in enumerate(food)]
    return ''.join(answer + ['0'] + answer[::-1])