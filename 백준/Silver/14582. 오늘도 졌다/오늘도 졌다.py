import sys
input = sys.stdin.readline

def baseball():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for i in range(1,len(A)+1):
        if sum(A[:i]) - sum(B[:i-1]) > 0:
            return 'Yes'
    return 'No'

print(baseball())