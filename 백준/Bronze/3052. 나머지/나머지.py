count = 0
answer = 0
num_list = []
while count < 10:
    a = int(input())
    num_list.append(a % 42)
    count += 1

for num in range(1, len(num_list)+1):
    pop_num = num_list.pop()
    if not pop_num in num_list:
        answer += 1

print(answer)