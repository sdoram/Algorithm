def solution(before, after):
    before_list = []
    after_list = []
    for i in before:
        before_list.append(ord(i))
    for i in after:
        after_list.append(ord(i))
    before_list.sort()
    after_list.sort()
    if before_list == after_list:
        return 1
    else:
        return 0

