input()

skill = input()
skill_dict = {}

for s in skill:
    if s not in skill_dict:
        if s == 'R' and 'L' not in skill_dict:
            break
        elif s == 'K' and 'S' not in skill_dict:
            break
        skill_dict[s] = 1
    elif s in skill_dict:
        if s == 'R' and skill_dict['R'] == skill_dict['L']:
            break
        elif s == 'K' and skill_dict['K'] == skill_dict['S']:
            break
        skill_dict[s] += 1
        
print(sum([value for key, value in skill_dict.items() if key != 'L' and key != 'S']))