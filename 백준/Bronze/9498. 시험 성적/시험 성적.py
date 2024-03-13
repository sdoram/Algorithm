import sys
SCORE = int(sys.stdin.readline())
if SCORE >= 90:
    print('A')
elif SCORE >= 80:
    print('B')
elif SCORE >= 70:
    print('C')  
elif SCORE >= 60:
    print('D')
else:
    print('F')