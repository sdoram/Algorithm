N, K = map(int, input().split())
country = {}

for _ in range(N):
    c = list(map(int, input().split()))
    country[c[0]] = c[1:]

sorted_country = sorted([[key, value] for key, value in country.items()], 
                        key=lambda x:(x[1][0], x[1][1], x[1][2]), reverse=True)

ranking = {}
CURRENT_RANK = 1
rank_check = sorted_country[0][1]

for i, sc in enumerate(sorted_country, start=1):
    if rank_check != sc[1]:
        CURRENT_RANK = i
        ranking[sc[0]] = CURRENT_RANK
        rank_check = sc[1]
    else:
        ranking[sc[0]] = CURRENT_RANK
        
print(ranking[K])