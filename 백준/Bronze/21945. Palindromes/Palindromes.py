input()
N = input().split()
print(sum([int(n) for n in N if n == n[::-1]]))