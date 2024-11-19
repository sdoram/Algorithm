N = list(input() for _ in range(int(input())))
for S in N:
    if sum([1 if s.islower() else 0 for s in S ]) >= sum([1 if s.isupper() else 0 for s in S ]):
        if 10 >= len(S):
            if sum([1 if not s.isdigit() else 0 for s in S]):
                print(S)
                break