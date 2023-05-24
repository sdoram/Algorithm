n = int(input())
for i in range(1, n + 1):
    if i % 2 != 0:
        print(" ".join("*" * n))
    else:
        print("", " ".join("*" * n))
