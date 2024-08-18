for _ in range(int(input())):
    num_list = list(map(int, input().split()))
    gcd_dict = {}
    
    for num in num_list:
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                if i < num//i:
                    if num//i not in gcd_dict:
                        gcd_dict[num//i] = [num]
                    else:
                        gcd_dict[num//i] += [num]
                if i not in gcd_dict:
                    gcd_dict[i] = [num]
                else:
                    gcd_dict[i] += [num]
    print(max([key for key, value in gcd_dict.items() if len(value) >= 2]))