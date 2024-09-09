import sys

input = sys.stdin.readline

ball_weight_dict = {}
for _ in range(int(input())):
    M =  list(map(int, input().split()))
    if M[0] == 1:
        if M[2] not in ball_weight_dict:
            ball_weight_dict[M[2]] = M[1]
    else:
        print(ball_weight_dict[M[1]])