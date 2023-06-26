hour, minute = map(int, input().split())
cook_minute = int(input())
total_minute = hour * 60 + minute + cook_minute
print(total_minute // 60 % 24, total_minute % 60)