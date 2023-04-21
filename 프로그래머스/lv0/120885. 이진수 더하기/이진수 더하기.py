def solution(bin1, bin2):
    # bin1, bin2는 문자열
    # return은 bin1과 bin2를 이진수로 더한 값
    # bin
    sum_bin = int(bin1, 2) + int(bin2, 2)
    answer = bin(sum_bin)[2:]
    
    return answer