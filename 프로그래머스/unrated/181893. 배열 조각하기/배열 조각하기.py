def solution(arr, query):
    # 짝수 arr에서 auery[i]번 인덱스 제외 query[i]번 인덱스 뒷부분 자르기
    # 홀수 arr에서 auery[i]번 인덱스 제외 query[i]번 인덱스 앞부분을 자르기
    # return은 남은 arr의 배열 
    for i,q in enumerate(query):
        arr = arr[:q+1] if i % 2 == 0 else arr[q:]
        # else:
        #     arr = arr[q:]
    return arr