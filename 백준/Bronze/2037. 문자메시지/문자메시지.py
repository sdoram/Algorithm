import sys
input = sys.stdin.readline
KEYBOARD = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], 
            ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
            ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
p, w = map(int, input().split())
INPUT_WORD = input().rstrip()
TIME = p*(INPUT_WORD.count(' ')) # 공백에 따른 시간 미리 삽입
for n, i in enumerate(INPUT_WORD):
    for k in KEYBOARD:
        if i in k:
            # 첫번째 입력이 아니고 이전 입력이 같은 자판인 경우 +w초
            TIME += p*(k.index(i)+1)+w if n != 0 and INPUT_WORD[n-1] in k else p*(k.index(i)+1)
print(TIME)
