team = [list(input().split()) for _ in range(3)]
team = [[int(t[0]), int(t[1]), t[2]] for t in team]
print(*sorted([t[1] % 100 for t in team]), sep='')
print(*[t[2][0] for t in sorted(team, reverse=True)], sep='')