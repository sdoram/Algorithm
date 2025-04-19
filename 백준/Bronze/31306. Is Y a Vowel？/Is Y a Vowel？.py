a = input()
b = sum([a.count('a'), a.count('e'), a.count('i'), a.count('o'), a.count('u')])
print(b, sum([b, a.count('y')]))