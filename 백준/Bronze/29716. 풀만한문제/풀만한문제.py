import sys
input = sys.stdin.readline

J, N = map(int, input().split())

quiz = [sum([4 if i.isupper() else 2 if i.isdecimal() or i.islower() else 1 
             for i in input().rstrip()]) for _ in range(N)]

print(sum([1 for q in quiz if J >= q]))