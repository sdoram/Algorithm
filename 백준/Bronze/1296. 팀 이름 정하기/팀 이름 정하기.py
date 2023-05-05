name = input()
team_names = []
for _ in range(int(input())):
    team_names.append(input())
winner = {}
for team in team_names:
    L = name.count('L')+team.count('L')
    O = name.count('O')+team.count('O')
    V = name.count('V')+team.count('V')
    E = name.count('E')+team.count('E')
    per = (((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
    if per not in winner:
        winner[per] = [team]
    else:
        winner[per] += [team]
print(sorted(winner[sorted(winner, reverse=True)[0]])[0])
