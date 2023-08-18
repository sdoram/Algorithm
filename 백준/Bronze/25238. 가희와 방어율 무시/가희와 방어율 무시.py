a, b = map(int, input().split())
print(0 if (100 - b) * 0.01 * a >= 100 else 1)