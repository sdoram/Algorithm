def solution(a, b):
    months = [0, 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[(sum(months[:a+1])+b) % 7]