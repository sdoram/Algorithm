input()
print('yummy' if len(set([C for C in list(input().split()) if 'eseehC' in C[:-7:-1]])) >= 4 else 'sad')