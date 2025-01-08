input()

Q = 0
while True:
    A = input()
    if A == '고무오리 디버깅 끝':
        break
    elif A == '문제':
        Q += 1
    else:
        if Q == 0:
            Q += 2
        else:
            Q -= 1
print('고무오리야 사랑해' if Q == 0 else '힝구')