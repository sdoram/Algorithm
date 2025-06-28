n = int(input())
x = input()
y = input()
print(len([1 for i in range(n) if x[i] != y[i]]))