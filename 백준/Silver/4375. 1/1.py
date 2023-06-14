from sys import stdin

while True:
    try:
        n = int(stdin.readline().strip())
    except ValueError:
        break
    i = 1
    COUNT = 1
    while i % n != 0:
        i = i * 10 + 1
        COUNT += 1
    print(COUNT)