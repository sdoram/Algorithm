def numbers_game(num):
    while len(num) != 1:
        num = str(sum([int(n) for n in num]))
    return num

while True:
    num = input()
    if num == '0':
        break
    print(numbers_game(num))