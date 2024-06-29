for _ in range(int(input())):
    password_massage = input()
    
    h = int(len(password_massage)**0.5)
    piece_massage = [password_massage[h*m: h*(m+1)] for m in range(h)]
    
    print(*[piece_massage[j][i] for i in range(h)[::-1] for j in range(h)], sep='')