charge_dict = {}
for _ in range(int(input())):
    t, n = input().split()
    time = list(map(int, t.split(':')))
    if n not in charge_dict:
        charge_dict[n] = time[0] * 60 + time[1]
    else:
        charge_dict[n] += time[0] * 60 + time[1]

charge_list = sorted([[key, max(((value-101) // 50 + 1) * 3, 0) + 10] for key, value in charge_dict.items()], key=lambda x: (-x[1], x[0]))

for c in charge_list:
    print(' '.join([c[0], str(c[1])]))