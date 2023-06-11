N, M = map(int, input().split())
persons_set = set()
unknown_set = set()
for _ in range(N + M):
    name = input()
    if name not in persons_set:
        persons_set.add(name)
    else:
        unknown_set.add(name)
print(len(unknown_set))
print("\n".join(sorted(unknown_set)))
