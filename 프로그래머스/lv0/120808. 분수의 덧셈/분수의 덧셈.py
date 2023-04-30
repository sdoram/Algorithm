def solution(numer1, denom1, numer2, denom2):
    numer = 0

    # 분모 공배수로 곱하기
    denom = denom1 * denom2

    # 분자
    numer1 = numer1 * denom / denom1
    numer2 = numer2 * denom / denom2

    numer = int(numer1 + numer2)

    # 공약수 찾기
    number = 0
    while number < 1000:
        for n in range(1, 1000):
            number += 1
            # 나눴을 때 소수점 존재 확인
            if numer / n == int(numer / n) and denom / n == int(denom / n):
                numer = numer / n
                denom = denom / n
            continue

    answer = [numer, denom]
    return answer