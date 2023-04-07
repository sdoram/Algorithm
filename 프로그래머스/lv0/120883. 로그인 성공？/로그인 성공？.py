def solution(id_pw, db):
    answer = ''
    for db_unit in db:
        if id_pw[0] == db_unit[0]:
            answer = "wrong pw"
            if db_unit[1] == id_pw[1]:
                answer = "login"
            return answer
    else:
        answer = "fail"        
    return answer