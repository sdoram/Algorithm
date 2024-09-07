def rainbow_dance():
    log_dict = {'ChongChong':True}
    for _ in range(int(input())):
        A, B = input().split()
        if A not in log_dict:
            log_dict[A] = False
        if B not in log_dict:
            log_dict[B] = False
        if sum([log_dict[A], log_dict[B]]):
            log_dict[A] = True
            log_dict[B] = True
    return sum(log_dict.values())

print(rainbow_dance())