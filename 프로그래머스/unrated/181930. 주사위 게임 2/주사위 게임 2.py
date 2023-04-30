def solution(a, b, c):
    # abc 모두 다르면 a+b+c
    # 두 숫자가 같으면 a+b+c * a**2+b**2+C**2
    # 세 숫자가 같으면 a+b+c * a**2+b**2+C**2 * a**3+b**3+C**3
    answer = 0
    if a == b == c:
        answer += (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    elif a != b != c != a:
        answer += a+b+c
    else:
        answer += (a+b+c) * (a**2+b**2+c**2)
    return answer