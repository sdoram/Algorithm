S = [int(input()) for _ in range(3)]
if sum(S) != 180:
    print("Error")
elif len(set(S)) == 3:
    print("Scalene")
elif len(set(S)) == 2:
    print("Isosceles")
elif len(set(S)) == 1:
    print("Equilateral")
