input()
M = int(input())
material_dict = {}
material = list(map(int, input().split()))
for m in material:
    if m not in material_dict:
        material_dict[m] = 1
    else:
        material_dict[m] += 1
        
print(sum([min([material_dict[M-k], v]) for k, v in material_dict.items() if M-k in material_dict]) // 2)