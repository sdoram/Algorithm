input()
print(''.join([s.lower() if s.isupper() else s.upper() for s in input()]))