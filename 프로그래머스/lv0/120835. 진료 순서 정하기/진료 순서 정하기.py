def solution(emergency):
    # 매개변수는 정수를 원소로 하는 배열
    # return은 순서를 조작하지 않고 원소를 통해서 순서를 나타내기
    # ::으로 복사하고 for, index를 통해서 원본 조작?
    sort_emergency = sorted(emergency, reverse=True)
    answer = emergency[::]
    for idx, eme in enumerate(sort_emergency, 1):
        answer[emergency.index(eme)] = idx
    return answer