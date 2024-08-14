A, P = input().split()
num_dict = {A:1}
while True:
    num = ''.join(str(sum([int(a)**int(P) for a in A])))
    if num not in num_dict:
        num_dict[num] = 1
    elif num_dict[num] == 2:
        break
    else:
        num_dict[num] += 1
    A = num
print(sum([v for v in num_dict.values() if v == 1]))