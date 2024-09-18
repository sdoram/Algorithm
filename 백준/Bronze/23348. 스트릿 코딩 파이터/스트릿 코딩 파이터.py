A, B, C = map(int, input().split())

club_score = []
for _ in range(int(input())):
    club = 0
    for _ in range(3):
        N = list(map(int, input().split()))
        club += A*N[0] + B*N[1] + C*N[2]
    club_score.append(club)
print(max(club_score))