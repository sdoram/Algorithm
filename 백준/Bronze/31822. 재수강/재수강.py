code = input()[:5]
subject = [input()[:5] for _ in range(int(input()))]
print(sum([1 for s in subject if s == code]))