def solution(box, n):
    # box는 박스 크기, n은 주사위 크기
    # 가로, 세로를 먼저 체크하고 높이를 체크
    answer = 0
    height_count = 0
    width_count = 0
    length_count = 0
    
    while True:
        # 박스의 높이가 주사위보다 길고
        if box[2] >= n * (height_count+1):
            height_count += 1
            continue
            
        # 박스의 가로가 주사위 보다 길면
        if box[0] >= n * (width_count+1):
            width_count += 1
            continue
        
        # 박스의 세로가 주사위 보다 길면
        if box[1] >= n * (length_count+1):
            length_count += 1
            continue
        answer = width_count * length_count * height_count
        return answer