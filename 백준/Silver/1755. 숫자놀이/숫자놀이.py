number = {'0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine'}

M, N = map(int, input().split())

number_list = sorted([[' '.join([number[n] for n in num]), num] for num in [str(i) for i in range(M, N+1)]], key=lambda x:x[0])

for i, num in enumerate(number_list, start=1):
    if i % 10 == 0:
        print(num[1])
    else:
        print(num[1], end=' ')