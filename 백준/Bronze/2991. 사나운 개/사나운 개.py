import sys
input = sys.stdin.readline
A, B, C, D = map(int, input().split())
PERSONS = list(map(int, input().split()))
for i in PERSONS:
    count = 0
    if  i % (A+B) != 0 and i % (A+B) <= A:
        count += 1
    if  i % (C+D) != 0 and i % (C+D) <= C:
        count += 1
    print(count)