stores = [list(map(int, input().split())) for _ in range(int(input()))]
available_stores = [s[1] for s in stores if s[0] <= s[1]]
print(min(available_stores) if len(available_stores) > 0 else -1)