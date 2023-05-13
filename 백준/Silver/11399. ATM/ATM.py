N = int(input())
num_list = sorted(list(map(int, input().split())))
print(sum([sum(num_list[: num + 1]) for num in range(N)]))
