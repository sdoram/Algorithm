a = int(input())
count = 0
num_list = []
while a > count:
    count += 1
    num_list.append(int(input()))

num_list.sort()

for num in num_list:
    print(num)