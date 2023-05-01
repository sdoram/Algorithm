def solution(s):
    answer = ''
    for n in set(s):
        # 첫번째 index 찾기
        first_index = s.index(n)
        # 두번째 index 찾기 시도
        try:
            _ = s.index(n, first_index+1)
        # 두번째 index가 없을 경우 except ValueError:
        except ValueError:
            answer += n
    return ''.join(sorted(answer))