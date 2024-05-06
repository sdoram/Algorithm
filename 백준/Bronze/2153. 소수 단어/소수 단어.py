import sys, string
input = sys.stdin.readline
ALPHABET = list(string.ascii_letters)
NUMBER = sum([ALPHABET.index(a)+1 for a in input().rstrip()])

def find_prime_num(n):
    for i in range(2, int(n**0.5+1)): # 정수로 바꿔 for문이 고장나지 않도록 한 후 올림을 위해 +1
        if n % i == 0:
            return 'It is not a prime word.' # 소수가 아닌 경우
    return 'It is a prime word.' # 소수인 경우

print(find_prime_num(NUMBER))