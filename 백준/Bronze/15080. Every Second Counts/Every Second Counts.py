start_time = list(map(int, input().split(":")))
end_time = list(map(int, input().split(":")))
start_second = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
end_second = end_time[0] * 3600 + end_time[1] * 60 + end_time[2]
if end_second < start_second:
    end_second += 24 * 3600
print(end_second - start_second)