n = int(input())
breakdown_list = [int(input()) for _ in range(n)]
print(abs(min([sum(breakdown_list[:i]) for i in range(n+1)])))