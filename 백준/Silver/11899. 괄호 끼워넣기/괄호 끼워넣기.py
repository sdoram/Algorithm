S = input()
parenthesis = {'(':0,
     ')':0}

for i in S:
    if i == ')':
        if parenthesis['('] == 0:
            parenthesis[')'] += 1
        parenthesis['('] = max(parenthesis['(']-1, 0)
    else:
        parenthesis['('] += 1


print(parenthesis['('] + parenthesis[')'])
