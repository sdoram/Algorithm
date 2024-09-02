def prime_number(N):
    for n in range(2, int(N**0.5)+1):
        if N % n == 0:
            return prime_number(N+1)
    return N if N >= 2 else 2

for _ in range(int(input())):
    print(prime_number(int(input())))