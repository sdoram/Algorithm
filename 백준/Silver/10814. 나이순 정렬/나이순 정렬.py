members = {}
for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    if age not in members:
        members[age] = [name]
    else:
        members[age] += [name]
sorted_members = sorted(members)
for num in sorted_members:
    for n in members[num]:
        print(num, n)