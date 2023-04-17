a, b = input().split()
reverse_a = ''
reverse_b = ''
for i in a[::-1]:
    reverse_a += i
for i in b[::-1]:
    reverse_b += i
reverse_a = int(reverse_a)
reverse_b = int(reverse_b)
if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)
