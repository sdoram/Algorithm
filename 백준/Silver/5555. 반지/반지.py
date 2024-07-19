import sys

input = sys.stdin.readline 
word = input().rstrip()

rings = [input().rstrip() for _ in range(int(input()))]
print(sum([1 if word in r[11-len(word):]+r else 0 for r in rings]))