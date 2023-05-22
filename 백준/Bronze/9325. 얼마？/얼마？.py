for _ in range(int(input())):
    car_price = int(input())
    for _ in range(int(input())):
        x, y = map(int, input().split())
        car_price += x * y
    print(car_price)