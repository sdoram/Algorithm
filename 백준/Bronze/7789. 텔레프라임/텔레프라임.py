import sys
PHONE_NUMBER, NUM = sys.stdin.readline().split()

def find_prime_num(n):
    n = int(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print('Yes' if sum([find_prime_num(PHONE_NUMBER), find_prime_num(NUM+PHONE_NUMBER)]) == 2 else 'No')