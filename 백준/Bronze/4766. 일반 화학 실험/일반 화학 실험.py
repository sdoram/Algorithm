import sys
NOW_TEMPERATURE = 0
COUNT = 0
while True:
    TEMPERATURE = float(sys.stdin.readline())
    if TEMPERATURE == 999:
        break
    if COUNT != 0:
        print("{:.2f}".format(TEMPERATURE - NOW_TEMPERATURE))
    NOW_TEMPERATURE = TEMPERATURE
    COUNT += 1