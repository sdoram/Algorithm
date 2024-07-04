dad_bird = input().split()
mom_bird = input().split()

children = {}

def find_children(parents):
    for p in parents:
        for db in dad_bird:
            if p not in children:
                children[p] = [db]
            elif db not in children[p]:
                children[p] += [db]
        for mb in mom_bird:
            if p not in children:
                children[p] = [mb]
            elif mb not in children[p]:
                children[p] += [mb]
                
find_children(dad_bird)
find_children(mom_bird)

children_list = sorted(sum([[[key, v] for v in value] for key, value in children.items()], []), key=lambda x:(x[0], x[1]))

for c in children_list:
    print(*c)