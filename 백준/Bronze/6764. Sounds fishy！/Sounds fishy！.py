detection = [int(input()) for _ in range(4)]
print('Fish At Constant Depth' if len(set(detection)) == 1
    else 'Fish Rising' if sorted(detection) == detection and len(set(detection)) == 4
    else 'Fish Diving' if sorted(detection, reverse=True) == detection and len(set(detection)) == 4
    else 'No Fish')
