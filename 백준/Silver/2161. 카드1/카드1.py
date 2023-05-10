N = int(input())
card_list = [n for n in range(1,N+1)]
drop_card_list = []
while True:
    drop_card_list.append(card_list.pop(0))
    try:
        card_list.append(card_list.pop(0))
    except IndexError:
        print(*drop_card_list)
        break