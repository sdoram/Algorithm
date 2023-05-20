for _ in range(int(input())):
    revenue, ad_revenue, ad = map(int, input().split())
    if ad_revenue == (revenue + ad):
        print("does not matter")
    elif ad_revenue > (revenue + ad):
        print("advertise")
    else:
        print("do not advertise")