n = int(input())
k = 60 + int(input())
print((n-k) * 3000 + k * 1500 if n > k else n * 1500)