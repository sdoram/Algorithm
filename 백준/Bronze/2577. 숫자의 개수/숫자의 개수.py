a = int(input())
b = int(input())
c = int(input())
# 0번부터 9번까지 만들고 그뒤에 중복이 생기면 +1 추가해야함
total = a * b * c
num_dict = {'0': 0, '1': 0, '2': 0, '3': 0,
            '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for num in str(total):
    if num in num_dict:
        num_dict[num] += 1
sort_num_dict = sorted(num_dict.items())

for _ in range(len(sort_num_dict)):
    print(sort_num_dict[_][1])
