# 같은 눈 3개 10,000+(주사위 눈)*1000
# 같은 눈 2개 1,000+(주사위 눈)*100
# 같은 눈 없음 (가장 큰 눈)*100

num_list = input().split()
num_list.sort()
a = int(num_list[0])
b = int(num_list[1])
c = int(num_list[2])

if a == b == c:
    print(10000+(a*1000))
elif a == b or a == c:
    print(1000+(a*100))
elif b == c:
    print(1000+(b*100))
else:
    print(c*100)