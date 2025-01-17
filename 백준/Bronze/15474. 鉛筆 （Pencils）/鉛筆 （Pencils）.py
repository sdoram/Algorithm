A, B, C, D, E = map(int, input().split())
F = A // B * C if A % B == 0 else (A // B + 1) * C
G = A // D * E if A % D == 0 else (A // D + 1) * E
print(min(F, G))