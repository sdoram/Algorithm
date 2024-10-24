for _ in range(int(input())):
    coin = input()
    coin_dict = {'TTT': 0,
                 'TTH': 0,
                 'THT': 0,
                 'THH': 0,
                 'HTT': 0,
                 'HTH': 0,
                 'HHT': 0,
                 'HHH': 0
                 }
    for i in range(38):
        coin_dict[coin[i:i+3]] += 1
    print(' '.join([str(c) for c in coin_dict.values()]))