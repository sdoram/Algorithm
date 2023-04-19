total_score = 0
for _ in range(5):
    a = int(input())
    if a < 40:
        a = 40
    total_score += a

print(total_score//5)
