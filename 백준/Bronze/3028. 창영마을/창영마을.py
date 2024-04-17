import sys
MIX_LIST = sys.stdin.readline().rstrip()
CURRENT_LOCATION = 1
for c in MIX_LIST:
    if CURRENT_LOCATION == 1:
        if c == 'A':
            CURRENT_LOCATION += 1
        elif c == 'C':
            CURRENT_LOCATION += 2
    elif CURRENT_LOCATION == 2:
        if c == 'A':
            CURRENT_LOCATION -= 1
        elif c == 'B':
            CURRENT_LOCATION += 1
    else:
        if c == 'B':
            CURRENT_LOCATION -= 1
        elif c == 'C':
            CURRENT_LOCATION -= 2
print(CURRENT_LOCATION)