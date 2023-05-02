while True:
    num = input()
    if num == '0':
        break
    answer = len(num)-1+2
    for n in num:
        if n == '1':
            answer += 2
        elif n == '0':
            answer += 4
        else:
            answer += 3
    print(answer)