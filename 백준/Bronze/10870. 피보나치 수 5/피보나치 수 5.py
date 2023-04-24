n = int(input())
first_num = 0
second_num = 1
answer = 0
while n > 0:
    first_num, second_num = second_num, first_num+second_num
    answer = first_num
    n -= 1
print(answer)