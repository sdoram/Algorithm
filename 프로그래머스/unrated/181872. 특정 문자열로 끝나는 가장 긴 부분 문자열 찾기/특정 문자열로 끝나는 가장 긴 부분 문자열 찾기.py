def solution(myString, pat):
    answer = []
    p = -myString[::-1].index(pat[::-1])
    return myString[:p if p != 0 else len(myString):]