name = input()
L, O, V, E = 0, 0, 0, 0
for x in name:
    if x == 'L':
        L += 1
    elif x == 'O':
        O += 1
    elif x == 'V':
        V += 1
    elif x == 'E':
        E += 1
LOVE = [L, O, V, E]
k = int(input())
maxScore = 0
fTeamName = ''

for i in range(k):
    teamName = input()
    for x in teamName: 
        if x == 'L':
            L += 1
        elif x == 'O':
            O += 1
        elif x == 'V':
            V += 1
        elif x == 'E':
            E += 1
    score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    count = 0
    if score > maxScore:
        fTeamName = teamName
        maxScore = score
    elif score == maxScore:
        for i in range(min(len(teamName), len(fTeamName))):
            if ord(teamName[i]) != ord(fTeamName[i]):
                if ord(teamName[i]) < ord(fTeamName[i]):
                    fTeamName = teamName 
                count = 1
                break
        if count == 0:
            if len(teamName) < len(fTeamName):
                fTeamName = teamName 
        if fTeamName == '':
            fTeamName = teamName
    L, O, V, E = LOVE
print(fTeamName)