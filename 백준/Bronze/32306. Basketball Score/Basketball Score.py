A, B, C = map(int, input().split())
D, E, F = map(int, input().split())
one_score = A + B * 2 + C * 3
two_score = D + E * 2 + F * 3
print(0 if one_score == two_score else 1 if one_score > two_score else 2)