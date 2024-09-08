warning_count = 0
pickup_list = [input() for _ in range(int(input()))]
children = {pickup:0 for pickup in pickup_list}
for pickup in pickup_list:
    if sum(children.values()) - children[pickup] < children[pickup]:
        warning_count += 1
    children[pickup] += 1
print(warning_count)