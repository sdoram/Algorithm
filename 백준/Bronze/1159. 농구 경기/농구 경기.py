last_name_dict = {}
for _ in range(int(input())):
    last_name = input()[0]
    if last_name in last_name_dict:
        last_name_dict[last_name] += 1
    else:
        last_name_dict[last_name] = 1
name = ""
for k, v in sorted(last_name_dict.items()):
    if v >= 5:
        name += k
print(name if name else "PREDAJA")
