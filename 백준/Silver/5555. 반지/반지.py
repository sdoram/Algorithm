import sys

input = sys.stdin.readline 
word = input().rstrip()

rings = [input().rstrip() for _ in range(int(input()))]
print(sum([1 if word in r[len(r)-len(word)+1:]+r else 0 for r in rings]))