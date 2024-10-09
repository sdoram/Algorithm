N = input()
number = {i:0 for i in range(10)}

for n in N:
    if n == '9':
        number[6] += 1
    else:
        number[int(n)] += 1
number[6] = (number[6]+1) // 2
print(max(number.values()))