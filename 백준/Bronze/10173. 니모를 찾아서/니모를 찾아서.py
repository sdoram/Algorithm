import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == 'EOI':
        break
    sentence = sentence.upper()
    if 'NEMO' in sentence:
        print('Found')
    else:
        print('Missing')