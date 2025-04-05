A = int(input())
B = int(input())
if B <= A:
    print('Congratulations, you are within the speed limit!')
else:
    if B >= A + 31:
        print('You are speeding and your fine is $500.')
    elif B >= A + 21:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $100.')