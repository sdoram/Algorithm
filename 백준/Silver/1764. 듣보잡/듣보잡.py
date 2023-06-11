N, M = map(int, input().split())
persons = {}
for _ in range(N + M):
    name = input()
    if name not in persons:
        persons[name] = 1
    else:
        persons[name] += 1
unknown_list = [i[0] for i in sorted(persons.items()) if i[1] == 2]
print(len(unknown_list))
print("\n".join(unknown_list))
