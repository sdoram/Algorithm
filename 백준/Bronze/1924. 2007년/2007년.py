day_of_the_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
months = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day = map(int, input().split())
days = sum(months[:month+1])+day
print(day_of_the_week[days % 7])