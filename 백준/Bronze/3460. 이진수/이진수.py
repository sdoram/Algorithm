for _ in range(int(input())):
    n = bin(int(input()))[2:]
    print(" ".join([str(i) for i, v in enumerate(n[::-1]) if v == "1"]))
