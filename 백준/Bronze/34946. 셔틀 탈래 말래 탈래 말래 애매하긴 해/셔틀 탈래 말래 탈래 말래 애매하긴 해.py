A, B, C, D = map(int, input().split())
Shuttle = A+B
Walk = C
print('~.~' if D >= max(Shuttle, Walk) else 'Shuttle' if D >= Shuttle else 'Walk' if D >= Walk else 'T.T')