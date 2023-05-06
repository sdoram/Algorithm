def factorial(num):
    number = 1
    for n in range(1, num+1):
        number *= n
    return number


N, K = map(int, input().split())
n = factorial(N)
r = factorial(K)
m = factorial(N-K)
print(n // (r*(m)))