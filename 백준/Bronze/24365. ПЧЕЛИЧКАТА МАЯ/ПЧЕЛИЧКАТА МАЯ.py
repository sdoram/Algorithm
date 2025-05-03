A, B, C = map(int, input().split())
print(sum([A, B, C]) // 3 - B + (sum([A, B, C]) // 3 - A) * 2)