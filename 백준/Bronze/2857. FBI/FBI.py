person_list = []
for i in range(1, 6):
    person = input()
    if "FBI" in person:
        person_list.append(str(i))
print(" ".join(person_list) if len(person_list) != 0 else "HE GOT AWAY!")
