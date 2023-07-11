def solution(name, yearning, photo):
    return[sum([pho.count(n) * yearning[i] for i,n in enumerate(name)]) for pho in photo]
