def solution(order):
    # order는 문자열을 가진 배열 
    # 아메리카노 4500, 카페라테 5000, 메뉴만 적으면 차가운 것, 아무거나 = 아아
    # 핫,아이스 고려 X
    # 카페라테 5000, 아무거나=아아 아아= 4500
    # return 가격
    latte = len([i for i in order if 'latte' in i])
    return (len(order) - latte)* 4500 + (latte*5000)