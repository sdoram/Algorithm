while True:
    n = int(input())
    if n == -1:
        break
    num_list = [num for num in range(1, (n - 1) // 2 + 2) if n % num == 0]
    if n == 1:
        print(f"{n} is NOT perfect.")
    elif n == sum(num_list):
        print(f"{n} = {' + '.join(map(str, num_list))}")
    else:
        print(f"{n} is NOT perfect.")