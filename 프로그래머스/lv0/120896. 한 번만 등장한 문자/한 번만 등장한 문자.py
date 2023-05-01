def solution(s):
    # for문 = set()으로 중복을 제거하고 sorted()로 정렬된 s
    # i = count로 확인된 숫자가 1개인 변수
    return ''.join([i for i in sorted(s) if s.count(i) == 1])