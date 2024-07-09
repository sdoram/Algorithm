ten_years = ['6', '7', '8', '9', '0', '1', '2', '3','4', '5']
zodiac = ['I', 'J', 'K', 'L', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ]
N = int(input()) % 60
print(zodiac[N % 12] + ten_years[N % 10])
