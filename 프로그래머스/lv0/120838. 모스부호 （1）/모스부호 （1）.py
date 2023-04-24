def solution(letter):
    # split.(' ')으로 letter를 구분하고 일치하는 key값을 찾고 value를 answer에 추가
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    split_letter = letter.split(' ')
    for spl_let in split_letter:
        if spl_let in morse.keys():
            answer += morse[spl_let]
    return answer