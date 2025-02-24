input()
NEWS = input()
N, E, W, S = NEWS.count('N'), NEWS.count('E'), NEWS.count('W'), NEWS.count('S')
print(max(N, S) - min(N, S) + max(E, W) - min(E, W))