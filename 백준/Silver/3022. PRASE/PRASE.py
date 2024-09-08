warning_count = 0
pickup_list = [input() for _ in range(int(input()))]
children = {pickup:0 for pickup in pickup_list}
for i, pickup in enumerate(pickup_list, start=1):
    if sum(children.values()) - children[pickup] < children[pickup]:
        warning_count += 1
    children[pickup] += 1
print(warning_count)