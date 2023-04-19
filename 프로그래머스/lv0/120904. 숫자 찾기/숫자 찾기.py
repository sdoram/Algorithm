def solution(num, k):
    # num , k는 int 
    # return은 num에 k가 있으면 자릿수 return,
    # 없으면 -1 return 
    # num 과 k 를 str 변환하고
    # index
    str_num = str(num)
    str_k = str(k)
    try:  
        answer = str_num.index(str_k)+1
    except ValueError:
        answer = -1
    return answer