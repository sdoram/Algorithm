def solution(chicken):
    # 쿠폰10장 => 서비스 = 1마리 + 쿠폰 1장 
    
    answer = 0
    # 최초 쿠폰 개수
    coupon = chicken
    # 쿠폰이 10장이면 서비스 치킨 주문
    while coupon >= 10:
        # 쿠폰으로 주문 가능한 서비스 치킨
        answer += coupon // 10
        # 서비스 치킨으로 받은 쿠폰
        coupon = coupon//10 + coupon%10
    return answer