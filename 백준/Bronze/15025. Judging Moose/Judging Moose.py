a, b = map(int, input().split())
print('Not a moose' if a+b == 0 else f'Even {a+b}' if a == b else f'Odd {max(a,b)*2}')