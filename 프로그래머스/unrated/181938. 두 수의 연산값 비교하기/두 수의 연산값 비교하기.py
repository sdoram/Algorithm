def solution(a, b):
    case_1 = int(str(a) + str(b))
    case_2 = 2*a*b
    if case_1 > case_2:
        return case_1
    elif case_2 > case_1:
        return case_2
    else:
        return a+b