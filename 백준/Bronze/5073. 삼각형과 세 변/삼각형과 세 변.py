import sys
while True:
    TRIANGLE = sorted(map(int, sys.stdin.readline().split()))
    if TRIANGLE.count(0) == 3:
        break
    elif TRIANGLE.count(TRIANGLE[0]) == 3:
        print('Equilateral')
    elif TRIANGLE[0]+TRIANGLE[1] <= TRIANGLE[2]:
        print('Invalid')
    elif TRIANGLE.count(TRIANGLE[1]) == 2:
        print('Isosceles')
    else:
        print('Scalene') 
