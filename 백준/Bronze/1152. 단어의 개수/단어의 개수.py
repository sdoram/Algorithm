a = input().split(' ')
if a[0] == '':
    a.pop(0)
if a[-1] == '':
    a.pop(-1)
print(len(a))
