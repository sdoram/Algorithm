serial_list = []
for _ in range(int(input())):
    serial_list.append(input())
serial_list = sorted(serial_list)
serial_list = sorted(
    serial_list, key=lambda serial: sum([int(s) for s in serial if s.isdigit()])
)
serial_list = sorted(serial_list, key=len)
print("\n".join(serial_list))