import math

for _ in range(int(input())):
    M, N = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    vertical_table = [math.prod([table[n][m] for n in range(N)]) for m in range(M)]
    table_dict = {}
    for i, t in enumerate(vertical_table, start=1):
        if t not in table_dict:
            table_dict[t] = [i]
        else:
            table_dict[t] += [i]
    print(table_dict[max(table_dict.keys())][-1])