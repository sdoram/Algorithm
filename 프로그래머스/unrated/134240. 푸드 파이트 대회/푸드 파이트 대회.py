def solution(food):
    answer = [str(i)*(f//2) for i,f in enumerate(food)]
    answer.append('0')
    for f in sorted(answer[:-1:], reverse=True):
        answer.append(f)
    return ''.join(answer)