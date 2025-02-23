N = int(input())
plan = list(map(int, input().split()))
execution = list(map(int, input().split()))
print(len([1 for i in range(N) if plan[i] <= execution[i]]))