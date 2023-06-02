def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return myStr if myStr else ["EMPTY"]