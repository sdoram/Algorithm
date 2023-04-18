def solution(my_string):
    answer = ''
    ord_list = []
    for i in my_string:
            i = i.lower()
            ord_list.append(i)
    # sorted()를 통해서 리스트를 오름차순으로 정렬
    sort_list = sorted(ord_list)
    # 정렬한 ord_list를 for문으로 answer에 집어넣기
    for i in sort_list:
        answer += i
    return answer