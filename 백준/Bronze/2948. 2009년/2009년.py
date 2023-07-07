import datetime

day_list = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def weekday(month, day):
    return day_list[datetime.datetime(2009, month, day).weekday()]


day, month = map(int, input().split())
print(weekday(month, day))