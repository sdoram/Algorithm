print(
    sum([1 if int(input().replace("D-", "")) <= 90 else 0 for _ in range(int(input()))])
)
