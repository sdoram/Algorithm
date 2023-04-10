count = 0
num_list = []
while count < 28:
    count += 1
    a = int(input())
    num_list.append(a)

for n in range(1, 31):
    if n not in num_list:
        print(n)
