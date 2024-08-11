N, J, H = map(int, input().split())
count = 1
while True:
    if max(J, H) == min(J, H)+1 and max(J, H) % 2 == 0:
        print(count)
        break
    J = (J+1)//2
    H = (H+1)//2
    count += 1