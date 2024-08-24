import string
cows = input()

cow_dict = {a:[] for a in string.ascii_uppercase}
for i, cow in enumerate(cows):
    for c in cows[i+1:]:
        if cow not in cow_dict[cow]:
            if c not in cow_dict[cow]:
                cow_dict[cow].append(c)
            else:
                cow_dict[cow].remove(c)

print(sum([len(value)-1 for value in cow_dict.values()])//2)