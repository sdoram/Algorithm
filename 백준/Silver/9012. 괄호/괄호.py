def parenthesis_string(ps):
    ps_dict = {"(": 0, ")": 0}
    for p in ps:
        ps_dict[p] += 1
        if ps_dict["("] < ps_dict[")"]:
            return "NO"
    return "YES" if ps_dict["("] == ps_dict[")"] else "NO"


for _ in range(int(input())):
    print(parenthesis_string(input()))