while True:
    vote = input()
    if vote == '#':
        break
    if len(vote) <= vote.count('A')*2:
        print('need quorum')
    elif vote.count('Y') > vote.count('N'):
        print('yes')
    elif vote.count('N') > vote.count('Y'):
        print('no')
    else:
        print('tie')