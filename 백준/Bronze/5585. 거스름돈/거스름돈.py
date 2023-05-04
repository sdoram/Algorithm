change = 1000 - int(input())
answer = 0
while change != 0:
    answer += 1
    if change - 500 >= 0:
        change -= 500
    elif change - 100 >= 0:
        change -= 100
    elif change - 50 >= 0:
        change -= 50
    elif change - 10 >= 0:
        change -= 10
    elif change - 5 >= 0:
        change -= 5
    elif change - 1 >= 0:
        change -= 1
print(answer)