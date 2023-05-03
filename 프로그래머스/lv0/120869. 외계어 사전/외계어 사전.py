def solution(spell, dic):
    for d in dic:
        if ''.join(sorted(spell)) == ''.join(sorted(d)):
            return 1
    return 2