from sys import stdin

N, M = map(int, stdin.readline().split())
persons_set = set()
unknown_set = set()
for _ in range(N + M):
    name = stdin.readline().strip()
    if name not in persons_set:
        persons_set.add(name)
    else:
        unknown_set.add(name)
print(len(unknown_set))
print("\n".join(sorted(unknown_set)))