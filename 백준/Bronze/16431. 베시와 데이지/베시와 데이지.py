B = list(map(int, input().split()))
D = list(map(int, input().split()))
J = list(map(int, input().split()))

bessie = max(max(B[0], J[0]) - min(B[0], J[0]), max(B[1], J[1]) - min(B[1], J[1]))
daisy = max(D[0], J[0]) - min(D[0], J[0]) + max(D[1], J[1]) - min(D[1], J[1])
print('tie' if bessie == daisy else 'bessie' if daisy > bessie else 'daisy')