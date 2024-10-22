A, B = map(int, input().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

print(A * B // gcd(max(A, B), min(A, B)))