import sys

input = sys.stdin.readline

N = int(input())
dairy_products = sorted([int(input()) for _ in range(N)], reverse=True)
print(sum([sum(dairy_products[i*3:(i+1)*3])-dairy_products[i*3:(i+1)*3][2] for i in range(N//3)])
      + sum(dairy_products[len(dairy_products)-(N%3):]))