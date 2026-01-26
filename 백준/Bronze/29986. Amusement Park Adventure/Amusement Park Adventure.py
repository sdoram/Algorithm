N, H = map(int, input().split())
print(sum([1 for x in map(int, input().split()) if H >= x]))