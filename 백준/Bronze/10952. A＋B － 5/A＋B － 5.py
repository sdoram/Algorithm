answer = 0
while True:
    a, b = map(int, input().split())
    answer = a + b
    if answer == 0:
        break
    print(answer)
