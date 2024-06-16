input()

print(max([i+n for i, n in enumerate(sorted(map(int, input().split()), reverse=True), start=2)]))
