import sys

input = sys.stdin.readline

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    gcd_dict = {key: [] for key in numbers[1:]}
    
    for i in range(1, numbers[0]+1):
        for n in range(1, int(numbers[i]**0.5)+1):
            if numbers[i] % n == 0:
                gcd_dict[numbers[i]].append(n)
                if n != numbers[i] // n:
                    gcd_dict[numbers[i]].append(numbers[i] // n)
    
    gcd_sum = 0
    for i in range(1, numbers[0] + 1):
        for j in range(i + 1, numbers[0] + 1):  # j를 i+1로 수정하여 중복 제거
            gcd_sum += max(set(gcd_dict[numbers[i]]) & set(gcd_dict[numbers[j]]))
    
    print(gcd_sum)