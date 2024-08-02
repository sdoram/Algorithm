N = int(input())
potato = sorted(list(map(int, input().split())))
print(sum(potato[:N//2]), sum(potato)-sum(potato[:N//2]))