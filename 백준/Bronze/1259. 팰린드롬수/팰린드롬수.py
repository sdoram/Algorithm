while True:
    num = input()
    if num == '0':
        break
    else:
        revNum = num[::-1]
        judge = 'yes' if revNum == num else 'no'
        print(judge)