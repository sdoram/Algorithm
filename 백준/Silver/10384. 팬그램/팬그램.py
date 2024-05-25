import sys, string
input = sys.stdin.readline
alphabet = list(string.ascii_lowercase) # 대소문자가 함께 주어지지만, lower로 바꾸고 체크하기

def count_pangram(N):
    for n in range(1,N+1):
        word = input().lower()
        for i in range(1,4):
            for alp in alphabet:
                if alp in word:    
                    word = word.replace(alp, '', 1)
                else: # 알파벳이 없다면 i에 따라 다른 출력
                    if i == 1:
                        print(f'Case {n}: Not a pangram')
                    elif i == 2:
                        print(f'Case {n}: Pangram!')
                    elif i == 3:
                        print(f'Case {n}: Double pangram!!')
                    break
            else: # 알파벳이 모두 있는 경우
                if i == 3:
                    print(f'Case {n}: Triple pangram!!!')
                continue
            break
        
count_pangram(int(input()))