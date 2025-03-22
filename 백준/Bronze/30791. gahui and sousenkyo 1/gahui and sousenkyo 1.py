votes = list(map(int, input().split()))
print(len([1 for v in votes[1:] if votes[0] <= v + 1000]))