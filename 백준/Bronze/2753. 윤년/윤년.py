A = int(input())
# 4의 배수&not 100의 배수, 400의 배수

if A % 4 == 0 and A % 100 != 0:
    print(1)
elif A % 400 == 0:
    print(1)
else:
    print(0)