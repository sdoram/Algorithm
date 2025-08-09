a, b, c, d = map(int, input().split())
print('M' if a*b > c*d else 'E' if a*b == c*d else 'P')