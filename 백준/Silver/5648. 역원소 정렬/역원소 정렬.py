number = list()
count = 0
while True:
    try:
        for n in list(input().split()):
            if count == 0 and number == list():
                count += 1
            else:
                number.append(int(n[::-1]))
    except EOFError:
        break
for n in sorted(number):
    print(n)