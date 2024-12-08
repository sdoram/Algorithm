b = bin(int(input()))[2:]
print(1 if b[0] == '1' and b.count('1') == 1 else 0)