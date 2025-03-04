N = float(input())
K = float(input())
print('Underweight' if 18.5 > N/(K*K) else 'Normal weight' if 25 >= N/(K*K) else 'Overweight')