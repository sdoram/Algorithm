N = int(input())
# range(1,로 가장 앞자리는 제외하기)
for i in range(1, len(str(N))):
    # N % 10**i 해당하는 자리 수 뽑아오기
    # 10 ** (i - 1)로 일의 자리로 만들기
    if N % 10**i // 10 ** (i - 1) >= 5:
        # 올림하고 0으로 만들기
        N += 10**i - (N % 10**i)
    else:
        # 내림하고 0으로 만들기
        N -= N % 10**i
print(N)