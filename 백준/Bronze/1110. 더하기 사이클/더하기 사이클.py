num = int(input())
end_num = num
count = 0
while True:
    count += 1
    tens_digit = num // 10
    unit_digit = num % 10
    new_tens_digit = unit_digit * 10
    new_unit_digit = (tens_digit+unit_digit) % 10
    num = new_tens_digit + new_unit_digit
    if num == end_num:
        break
print(count)
