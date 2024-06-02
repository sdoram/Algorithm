for _ in range(int(input())):
    NUM = [*[bin(n)[2:].zfill(4) for n in range(1, 16)], *([bin(n)[2:].zfill(4) for n in range(2, 15)[::-1]])]
    N = (int(input())-1) % 28
    print(NUM[N].replace('0', 'V').replace('1', '딸기'))