souvenir = [list(map(int, input().split())) for _ in range(int(input()))]
print(*sum(sorted(souvenir, key=lambda x:(-x[0], x[1]))[:2], []))
print(*sum(sorted(souvenir, key=lambda x:(x[1], -x[0]))[:2], []))