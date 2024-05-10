import sys
while True:
    a1, a2, a3 = map(int, sys.stdin.readline().split())
    if [a1, a2, a3].count(0) == 3:
        break
    print('AP '+ str(a3 + a2 - a1) if a3 - a2 == a2 - a1 else 'GP '+ str(a3 * a2//a1))
    