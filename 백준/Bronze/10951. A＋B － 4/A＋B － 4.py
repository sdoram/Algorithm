answer = 0
while True:
    try:
        a, b = map(int, input().split())
        answer = a + b
        print(answer)
    except:
        break
