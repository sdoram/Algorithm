import sys
S = int(sys.stdin.readline())
NUM = 0
while S > NUM:
    NUM += 1
    S -= NUM
print(NUM)
    