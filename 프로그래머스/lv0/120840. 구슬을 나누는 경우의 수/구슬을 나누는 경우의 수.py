def solution(balls, share):
    # balls!
    # (balls-share)! * share!
    factorial_balls = 1
    factorial_share = 1
    factorial_bs = 1
    
    for b in range(1, balls+1):
        factorial_balls *= b
        
    for s in range(1, share+1):
        factorial_share *= s
    
    for bs in range(1, balls-share+1):
        factorial_bs *= bs
    return factorial_balls//(factorial_bs*factorial_share)