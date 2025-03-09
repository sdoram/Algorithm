N = int(input())
print(sum([sum([i, N//i]) if i != N//i else i for i in range(1, int(N**0.5)+1) if N % i == 0]))