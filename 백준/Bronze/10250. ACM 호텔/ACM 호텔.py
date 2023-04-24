T = int(input())
for _ in range(T):
    count = 1
    H, W, N = map(int, input().split())
    while True:
        N -= H
        if N <= 0:
            current_H = str(H + N)
            current_W = str(count)
            if len(current_W) < 2:
                current_W = f'0{current_W}'
            check_in = int(current_H+current_W)
            print(check_in)
            break
        count += 1
