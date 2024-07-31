def bit():
    N = int(input())
    K = int(input(),2)
    count = 0
    
    while True:
        if K == 0:
            return count
        K = K-(K&((~K)+1))
        count += 1
print(bit())
