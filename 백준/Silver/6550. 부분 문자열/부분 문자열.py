import sys

inputs = sys.stdin.readlines

def word_check(S, T):
    count = 0
    
    for s in S:
        if T.find(s, count) == -1:
            return 'No'
        count = T.find(s, count)+1
    return 'Yes'

for i in inputs():
    S, T = i.split()
    print(word_check(S, T))