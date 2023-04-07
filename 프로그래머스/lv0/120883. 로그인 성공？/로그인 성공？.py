def solution(id_pw, db):
    answer = ''
    for i in db:
        # 둘다 일치
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            return 'login'
        # id만 일치
        elif id_pw[0] == i[0]:
            return 'wrong pw'
        # 일치 X
        else:
            answer = 'fail'
    return answer