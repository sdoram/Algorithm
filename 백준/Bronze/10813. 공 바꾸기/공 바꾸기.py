# 바구니 n개, m번 공을 바꿈
# 각 바구니에는 바구니 번호와 같은 번호의 공이 존재
num_list = []
count = 0
num_one = 0
num_two = 0
answer = ''
str_num_list = []
n, m = map(int, input().split())
for num in range(1, n+1):
    num_list.append(num)

while m > count:
    count += 1
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    num_one = num_list[a]
    num_two = num_list[b]
    num_list[a] = num_two
    num_list[b] = num_one

for num in num_list:
    str_num_list.append(str(num))
answer = ' '.join(str_num_list)
print(answer)
