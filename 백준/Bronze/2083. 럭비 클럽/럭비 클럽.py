while True:
    person = input().split()
    if person == ["#", "0", "0"]:
        break

    if int(person[1]) > 17 or int(person[2]) >= 80:
        print(person[0], "Senior")
    else:
        print(person[0], "Junior")