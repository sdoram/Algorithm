import sys 

input = sys.stdin.readline

pandom = {'s':[],
          'e':[]}
for _ in range(int(input())):
    s, e = map(int, input().split())
    pandom['s'].append(s)
    pandom['e'].append(e)

print(max(max(pandom['s']) - min(pandom['e']), 0))