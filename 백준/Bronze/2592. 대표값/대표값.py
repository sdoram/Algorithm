import sys
NUM_LIST = [int(sys.stdin.readline()) for _ in range(10)]
MODE_COUNT = 0
for n in NUM_LIST:
    if NUM_LIST.count(n) > MODE_COUNT:
        MODE = n
        MODE_COUNT = NUM_LIST.count(n)
print(sum(NUM_LIST)//10, MODE, sep='\n')