n, f = map(int, input().split())
car_dict = dict()
for i in range(1, n+1):
    x, y = map(int, input().split())
    car_dict[(f - x) / y] = i
print(car_dict[min(car_dict)])