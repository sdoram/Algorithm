for i in range(1, int(input())+1):
    N = int(input())
    if N == 0:
        print(f'Case #{i}: INSOMNIA')
    else:
        num_list = set([int(n) for n in str(N)])
        count = 1
    
        while True:
            if len(num_list) == 10:
                print(f'Case #{i}: {N*count}')
                break
            count += 1
            num_list |= set([int(n) for n in str(N*count)])