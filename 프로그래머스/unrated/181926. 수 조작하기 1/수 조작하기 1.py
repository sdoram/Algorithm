def solution(n, control):
    control_dict = {"w":1,"s":-1,"d":10,"a":-10}
    return n+sum([control_dict[con] for con in control])