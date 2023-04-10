n, m = map(int, input().split())

count = 0
basket_ball_list = []
answer = 0
# 빈 바구니 생성
for num in range(1, n+1):
    basket_ball_list.append('0')

# m 번 만큼 반복
while m > count:
    count += 1
    i, j, k = map(int, input().split())
    for num in range(i-1, j):
        basket_ball_list[num] = str(k)

answer = ' '.join(basket_ball_list)
print(answer)