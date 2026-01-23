QALY = 0
for _ in range(int(input())):
    q, y = map(float, input().split())
    QALY += q * y
    
print(QALY)