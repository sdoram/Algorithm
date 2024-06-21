ring_dict = {}
for _ in range(int(input())):
    name, ring = input().split()
    if ring not in ring_dict:
        ring_dict[ring] = [name]
    else:
        ring_dict[ring] += [name]
        
couple = [name for ring, name in ring_dict.items() if ring != '-' and len(name) == 2]
if len(couple) == 0:
    print(0)
else:
    print(len(couple))
    for c in couple:
        print(*c)